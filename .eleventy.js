const slugify = require('slugify');
const fs = require('fs');
const path = require('path');

const read = file => fs.readFileSync(path.join(__dirname, file), 'utf8');

const parseTokens = () => {
  const defs = {};
  for (const [, name, value] of read('system/tokens.css')
    .matchAll(/(--ds-[a-z0-9-]+)\s*:\s*([^;}]+);/g)) {
    defs[name] = value.trim();
  }

  const resolve = (value, depth = 0) => {
    if (depth > 10) throw new Error(`Token alias chain too deep: ${value}`);
    return value.replace(/var\((--ds-[a-z0-9-]+)\)/g, (_, ref) => {
      if (!(ref in defs)) throw new Error(`Undefined token referenced: ${ref}`);
      return resolve(defs[ref], depth + 1);
    }).trim();
  };

  return Object.fromEntries(
    Object.entries(defs).map(([name, value]) => [name, resolve(value)])
  );
};

// Maps a Sass variable name to the custom property it aliases, following
// variable-to-variable aliases such as `$redForBlueLight: $redForWhite`.
const parseSassAliases = () => {
  const raw = {};
  for (const [, name, value] of read('system/partials/_variables.scss')
    .matchAll(/^\$([\w-]+):\s*([^;]+);/gm)) {
    raw['$' + name] = value.trim();
  }

  const aliases = {};
  for (const name of Object.keys(raw)) {
    let value = raw[name];
    for (let i = 0; value.startsWith('$') && i < 10; i++) value = raw[value];
    const match = /^var\((--ds-[a-z0-9-]+)\)$/.exec(value || '');
    if (match) aliases[name] = match[1];
  }
  return aliases;
};

const tokens = parseTokens();
const sassAliases = parseSassAliases();

module.exports = function (eleventyConfig) {
  eleventyConfig.setUseGitIgnore(false);
  eleventyConfig.addPassthroughCopy('src-site/styles');
  eleventyConfig.addPassthroughCopy('src-site/images');

  const filterAscending = (collection, glob) => {
    return collection.getFilteredByGlob(glob).sort((a, b) => {
      if (a.data.title < b.data.title) return -1;
      else if (a.data.title > b.data.title) return 1;
      else return 0;
    });
  }

  eleventyConfig.addCollection('basicsAscending', collection => {
    return filterAscending(collection, 'src-site/basics/*.md');
  });

  eleventyConfig.addCollection('componentsAscending', collection => {
    return filterAscending(collection, 'src-site/components/*.md');
  });

  eleventyConfig.addCollection('usageAscending', collection => {
    return filterAscending(collection, 'src-site/usage/*.md');
  });

  eleventyConfig.addPairedShortcode('note', function (content, title) {
    const slug = slugify(title).toLowerCase();
    return `
<aside class="site-note site-stack" style="--stack-space: 1rem" aria-labelledby="${slug}">
  <h3 id="${slug}">🗒️ ${title}</h3>
  <div class="site-stack">${content}</div>
</aside>`;
  });


  eleventyConfig.addPairedShortcode('ds-example', function (content) {
  var dark_content = content.replace(/id="/g, 'id="dark_');
  dark_content = dark_content.replace(/for="/g, 'for="dark_');
  return `
<div class="site-stack" style="--stack-space: 1rem">
<div class="site-stack">
<h2>Light theme</h2>
<div class="ds-scope">
<div class="ds-example-light" style="padding: 1em">
${content}
</div>
</div>
<h2>Dark theme</h2>
<small>Invoke the dark theme on any component by applying <code>class="ds-dark"</code> to a container element.</small>
<div class="ds-scope">
<div class="ds-dark ds-example-dark" style="padding: 1em">
${dark_content}
</div>
</div>
</div>
</div>

`;
  });

  eleventyConfig.addPairedShortcode('warning', function (content, title) {
    const slug = slugify(title).toLowerCase();
    return `
<aside class="site-note-warning site-stack" style="--stack-space: 1rem" aria-labelledby="${slug}">
  <h3 id="${slug}">⚠️ ${title}</h3>
  <div class="site-stack">${content}</div>
</aside>`;
  });

  /*eleventyConfig.addFilter('variable', function (data, name) {
    let vars = data.variables;
    console.log('vars:', typeof vars);
    console.log('name:', name);
    //let thevar = vars.find(v => v.value === name);
    //console.log('the var:', thevar);
    //return vars.find(v => v.name === name).compiledValue;
  });*/

  // Resolved value behind a Sass variable, e.g. {% var '$black' %}.
  eleventyConfig.addShortcode('var', function (name) {
    const token = sassAliases[name];
    return (token && tokens[token]) || 'undefined';
  });

  // The custom property a Sass variable aliases, e.g. {% cssvar '$black' %}.
  eleventyConfig.addShortcode('cssvar', function (name) {
    return sassAliases[name] || 'undefined';
  });

  // Resolved value of a token by property name, e.g. {% token '--ds-colour-text' %}.
  eleventyConfig.addShortcode('token', function (name) {
    return tokens[name] || 'undefined';
  });

  return {
    dir: {
      input: './src-site',
      output: './docs'
    },
    passthroughFileCopy: true
  };
};
