<template>
  <div> <!-- template can only have one root element -->
    <router-view />
  </div>

</template>

<script>
export default {
  name: 'App',
  components: {

  },
  data() {

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
  margin-top: 60px;
}
</style>
