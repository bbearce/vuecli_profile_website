<template>
  <div>
    <h1>Blog_List</h1>
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
      posts: null
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
