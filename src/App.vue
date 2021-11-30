<template>
  <div> <!-- template can only have one root element -->
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <NavBar/>
    <FrontPageVideo/>
  </div>

</template>

<script>
// import HelloWorld from './components/HelloWorld.vue' // demo from vue cli
import NavBar from './components/NavBar.vue'
import FrontPageVideo from './components/FrontPageVideo.vue'

export default {
  name: 'App',
  components: {
    // HelloWorld,
    NavBar,
    FrontPageVideo,
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
