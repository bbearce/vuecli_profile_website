<template>

    <div>
        <p>{{ $route.params.date }}</p>
        <div v-html="markdownToHTML" />
    </div>

</template>

<script>
import { marked } from 'marked';

export default {
    name: 'blog_post',
    components: {},
    mounted() {
        this.readMarkdownFile();
    },
    data(){
        return {
            markdown: '# init',
            year: null,
            month: null,
            day: null,
            blog_post: null,
            custom_js: false,
            custom_css: false
        }
    },
    computed: {
        markdownToHTML() {
        return marked(this.markdown);

        },

    },
    methods: {
        readMarkdownFile: function() {
        var self = this
        self.year = this.$route.params.date.slice(0,4);
        self.month = this.$route.params.date.slice(5,7);
        self.day = this.$route.params.date.slice(8,10);
        fetch(`/blog_posts/blog_metadata.json`)
            .then(function (res) { return res.text() })
            .then(res => {
                let blog_metadata = JSON.parse(res)
                blog_metadata.forEach((v, i, a) => {
                    // debugger
                    if (v.date === `${self.year}-${self.month}-${self.day}`) {
                        self.blog_post = v
                    }
                })
                self.markdown = res
            });  
        fetch(`/blog_posts/${self.year}/${self.month}/${self.day}/${self.day}.md`)
            .then(function (res) { return res.text() })
            .then(res => {
                self.markdown = res
            })
            .then(() => {
                if (self.blog_post['custom_js']) {
                    // Add custom JS for raw HTML
                    fetch(`/blog_posts/${self.year}/${self.month}/${self.day}/custom.js`)
                        .then(function (res) { return res.text() })
                        .then(res => {
                            let new_script_tag = document.createElement('script')
                            new_script_tag.innerHTML = res
                            document.body.appendChild(new_script_tag)
                        })
                }
                if (self.blog_post['custom_css']) {
                    // Add custom JS for raw HTML
                    fetch(`/blog_posts/${self.year}/${self.month}/${self.day}/custom.css`)
                        .then(function (res) { return res.text() })
                        .then(res => {
                            let new_css_tag = document.createElement('style')
                            new_css_tag.type = 'text/css';
                            new_css_tag.innerHTML = res
                            document.head.appendChild(new_css_tag)
                        })
                }
            })
        },
    }

}
</script>

<style>

</style>
