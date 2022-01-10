<template>
  <div>
    <h1>Blog</h1>
    <div v-html="markdownToHTML" />
    <button v-on:click="readMarkdownFile()">readMarkdownFile</button>
  </div>
</template>

<script>
// import data from '@/resources/data.json' //json import test
import { marked } from 'marked';

export default {
  name: 'blog',
  components: {},
  data() {
    return {
      markdown: "init"
    }
  },
  computed: {
    markdownToHTML() {
      // return marked("<h1>Hello World</h1>");
      console.log('markdownToHTML')
      // return marked(this.markdown);
      return marked(this.markdown);

      // return "<h1>Hello World</h1>"
    },
  },
  methods: {
    readMarkdownFile: function() {
      var self = this
      fetch("/blog_posts/01_2022/09.md")
        .then(function(res){ return res.text()})
        .then(res =>{
          console.log(res)
          self.markdown = res
        })
    },
  }
}
</script>
