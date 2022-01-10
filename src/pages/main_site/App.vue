<template>
  <div> <!-- template can only have one root element -->
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <!-- <FrontPageVideo/> -->
    <!-- <textarea v-model="markdown"></textarea>
    <div v-html="markdownToHTML"></div> -->
    <router-view />

  </div>

</template>

<script>
// import HelloWorld from './components/HelloWorld.vue' // demo from vue cli
// import NavBar from '@/components/NavBar.vue'
import { marked } from 'marked';
// import FrontPageVideo from '@/components/FrontPageVideo.vue'

export default {
  name: 'App',
  components: {
    // HelloWorld,
    // NavBar,
    // FrontPageVideo,
    // Foo
  },
  data() {
    return {
      markdown: "# hello world"
      }
  },
  computed: {
    markdownToHTML() {
      // return marked("<h1>Hello World</h1>");
      return marked(this.markdown);
      // return "<h1>Hello World</h1>"
    },
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
