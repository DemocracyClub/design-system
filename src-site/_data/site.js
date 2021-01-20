module.exports = function() {
  return {
    name: 'Democracy Club Design System',
    basedir: process.env.DESTINATION === 'github' ? 'https://DemocracyClub.github.io/design-system/' : '/',
  }
}