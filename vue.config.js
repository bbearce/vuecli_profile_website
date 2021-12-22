// vue.config.js
module.exports = {
    pages:{
        index: {
            entry: "src/pages/main/main.js",
            template: "public/index.html",
            filename: "index.html",
            title: "Index Page",
            chunks: ['chunk-vendors', 'chunk-common', 'index']
        },
        experiment: {
            entry: "src/pages/experiment/main.js",
            template: "public/experiment.html",
            filename: "experiment.html",
            title: "Experiment Page",
            chunks: ['chunk-vendors', 'chunk-common', 'experiment']
        },
    },
    devServer: {
        historyApiFallback: {
          rewrites: [
            { from: /\/index/, to: '/index.html' },
            { from: /\/experiment/, to: '/experiment.html' }
          ]
        }
      },
    // https://www.youtube.com/watch?v=agaC4oKn_0k
    css: {
        loaderOptions: {
            sass: {
                additionalData: `@import "@/assets/scss/_variables.scss";`,
            },
        },
    },
}