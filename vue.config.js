// vue.config.js
module.exports = {
    // https://www.youtube.com/watch?v=agaC4oKn_0k
    css: {
        loaderOptions: {
            sass: {
                additionalData: `@import "@/assets/scss/_variables.scss";`,
            },
        },
    },
}