<template>

  <div>
    <div class="card">
      <h2>{{ title }}</h2>
      <h4>{{ author }}</h4>
      <h5>{{ desc }} {{ date }}</h5>
      <a :href="'/main_site/blog_post/'+this.year+'-'+this.month+'-'+this.day">
        <img class="fakeimg" v-bind:src="'/blog_posts/'+this.year+'/'+this.month+'/'+this.day+'/logo.png'" style="height:200px;">
      </a>
      <p>Some text..</p>
    </div>
  </div>

</template>

<script>
export default {
    name: 'blog_list_entry',
    components: {},
    props: {"id": Number,
            "title": String,
            "desc": String,
            "author": String,
            "date": String,
            "image": String,
    },
    created() {
    },
    data() {
        return {
            year: this.date.slice(0,4),
            month: this.date.slice(5,7),
            day: this.date.slice(8,10),

        }
    }
}
</script>

<style>
body {
  font-family: Arial;
  padding: 20px;
  background: #f1f1f1;
}


/* Fake image */
.fakeimg {
  background-color: rgb(87, 87, 87);
  width: 20%;
  padding: 10px;
}

/* Add a card effect for articles */
.card {
  background-color: white;
  padding: 20px;
  margin-top: 20px;
}
</style>