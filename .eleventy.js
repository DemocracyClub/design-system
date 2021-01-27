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
      output: './_site'
    },
    passthroughFileCopy: true
  };
};