<template>
  <router-view />

</template>

<script>
export default {
  name: 'App',
  components: {

  },
  data() {
    return{
      background_image: '/portfolio/fall_large.jpg'
    }
  },
  computed: {

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
}
</style>
