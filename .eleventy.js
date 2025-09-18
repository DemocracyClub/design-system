const slugify = require('slugify');
const sassVars = require('./src-site/_data/sass.json').variables;

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

  eleventyConfig.addShortcode('var', function(name) {
    let theOne = sassVars.find(v => v.name === name);
    let value = theOne && theOne.compiledValue;
    return value ? value : 'undefined';
  });

  return {
    dir: {
      input: './src-site',
      output: './docs'
    },
    passthroughFileCopy: true
  };
};
