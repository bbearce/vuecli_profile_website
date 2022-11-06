<template>

  <div>
    <div class="card">
      <h2>{{ title }}</h2>
      <h4>{{ author }}</h4>
      <h5>{{ desc }} {{ date }}</h5>
      <a :href="'/main_site/blog_post/'+this.year+'-'+this.month+'-'+this.day">
        <img class="fakeimg" v-bind:src="'/blog_posts/'+this.year+'/'+this.month+'/'+this.day+'/logo.png'" style="height:200px;">
      </a>
      <p>{{ desc }}</p>
    </div>
  </div>

</template>

<script>
// https://www.w3schools.com/howto/howto_css_blog_layout.asp
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

<style scoped>
/* Fake image */
.fakeimg {
  background-color: rgb(87, 87, 87);
  width: 30%;
  width: 40%;
  padding: 10px;
}

/* Add a card effect for articles */
.card {
  background-color: #f1f3f4;
  padding: 20px;
  /* margin: 0px 200px 100px 200px; */
  margin: 0% 10% 10% 10%;
  border-radius: 1%;
  box-shadow: -2px 1px 8px 1px lightgrey;
}

@media only screen and (min-width: 1300px) {
  .card {
    margin: 0% 20% 10% 20%;
  }
}

@media only screen and (min-width: 1800px) {
  .card {
    margin: 0% 30% 5% 30%;
  }
}
</style>