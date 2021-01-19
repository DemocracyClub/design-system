module.exports = function (eleventyConfig) {
  eleventyConfig.setUseGitIgnore(false);
  eleventyConfig.addPassthroughCopy('src/styles');

  return {
    dir: {
      input: './src-site',
      output: './docs'
    },
    passthroughFileCopy: true
  };
};