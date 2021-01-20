module.exports = function (eleventyConfig) {
  eleventyConfig.setUseGitIgnore(false);
  eleventyConfig.addPassthroughCopy('src-site/styles');
  eleventyConfig.addPassthroughCopy('src-site/images');

  eleventyConfig.addCollection('basicsAscending', (collection) =>
    collection.getFilteredByGlob('src-site/basics/*.md').sort((a, b) => {
      if (a.data.title < b.data.title) return -1;
      else if (a.data.title > b.data.title) return 1;
      else return 0;
    })
  );

  eleventyConfig.addCollection('componentsAscending', (collection) =>
    collection.getFilteredByGlob('src-site/components/*.md').sort((a, b) => {
      if (a.data.title < b.data.title) return -1;
      else if (a.data.title > b.data.title) return 1;
      else return 0;
    })
  );

  return {
    dir: {
      input: './src-site',
      output: './_site'
    },
    passthroughFileCopy: true
  };
};