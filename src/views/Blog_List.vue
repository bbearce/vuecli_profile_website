<template>
  <div v-bind:style="{ 'background-image': 'url(' + background_image + ')', 'background-attachment':'fixed', 'background-size':'cover' }">
    <br>
    <Blog_List_Entry v-for="post in posts" 
      :key="post.id" 
      :title="post.title" 
      :desc="post.desc" 
      :author="post.author"
      :date="post.date"
      :image="post.image"
    />
  </div>
</template>

<script>
import Blog_List_Entry from '@/components/Blog_List_Entry.vue'

export default {
  name: 'blog_list',
  components: {
    Blog_List_Entry,
  },
  data() {
    return {
      posts: null,
      // background_image: '/portfolio/red_pink_flowers_forest.jpg'
      background_image: '/portfolio/fall_large.jpg'
    }
  },
  created() {
    // Dynamic routes for each blog post
    var THIS = this;
    fetch("/blog_posts/blog_metadata.json")
    .then(function(res){ return res.json() })
    .then(function(res){
        THIS.posts = res
    })
  },
}
</script>

<style scoped>

</style>
