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
            markdown : '# init',
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
        var year = this.$route.params.date.slice(0,4);
        var month = this.$route.params.date.slice(5,7);
        var day = this.$route.params.date.slice(8,10);
        fetch(`/blog_posts/${year}/${month}/${day}/${day}.md`)
            .then(function(res){ return res.text()})
            .then(res =>{
            self.markdown = res
            })
        },
    }

}
</script>

<style>

</style>
