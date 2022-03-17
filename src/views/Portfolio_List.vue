<template>
  <div v-bind:style="{ 'background-image': 'url(' + background_image + ')', 'background-attachment':'fixed', 'background-size':'cover' }">
    <br>
    <Portfolio_List_Entry v-for="project in projects" 
      :key="project.id" 
      :title="project.title" 
      :desc="project.desc" 
      :author="project.author"
      :date="project.date"
      :image="project.image"
      :link="project.link"
      :github="project.github"
    />
  </div>
</template>

<script>
import Portfolio_List_Entry from '@/components/Portfolio_List_Entry.vue'

export default {
  name: 'blog_list',
  components: {
    Portfolio_List_Entry,
  },
  data() {
    return {
      projects: null,
      background_image: '/portfolio/fire_spindly.jpg'
    }
  },
  created() {
    // Dynamic routes for each blog post
    var THIS = this;
    fetch("/portfolio/portfolio_metadata.json")
    .then(function(res){ return res.json() })
    .then(function(res){
        THIS.projects = res
    })
  },
}
</script>

<style scoped>

</style>