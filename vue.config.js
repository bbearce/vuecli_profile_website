// vue.config.js
module.exports = {
    pages:{
        'index': {
            entry: "./src/pages/front_page/main.js",
            template: "public/index.html",
            title: "Index Page",
            chunks: ['chunk-vendors', 'chunk-common', 'index']
        },
        'main_site': {
            entry: "./src/pages/main_site/main.js",
            template: "public/index.html",
            title: "Main Site",
            chunks: ['chunk-vendors', 'chunk-common', 'main_site']
        },
    },
    // https://www.youtube.com/watch?v=agaC4oKn_0k
    css: {
        loaderOptions: {
            sass: {
                additionalData: `@import "@/assets/scss/_variables.scss";`,
            },
        },
    },
    configureWebpack: {
        devtool: 'source-map'
    }
}