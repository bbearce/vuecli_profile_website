<template>

  <div>
    <div class="card">
      <h2>{{ title }}</h2>
      <h3>{{ desc }}</h3>
      <h4>{{ date }}</h4>
      <h5>{{ author }}</h5>
      <a :href="'/main_site/blog_post/'+this.year+'-'+this.month+'-'+this.day">
        <img class="blog_entry_cover_image" v-bind:src=image style="height:200px;">
      </a>
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
            day: this.date.slice(8, 10)
        }
    }
}
</script>

<style scoped>
h3 {
  text-align: center;
}
.blog_entry_cover_image {
  background-color: rgb(87, 87, 87);
  width: 50%;
  /* height: 40%; */
  padding: 10px;
}

/* Add a card effect for articles */
.card {
  background-color: #f1f3f4;
  padding: 20px;
  /* margin: 0px 200px 100px 200px; */
  margin: 0% 33% 10% 30%;
  border-radius: 1%;
  box-shadow: -2px 1px 8px 1px lightgrey;
}

@media only screen and (min-width: 1300px) {
  .card {
    margin: 0% 28% 10% 28%;
  }
}

@media only screen and (min-width: 1400px) {
  .card {
    margin: 0% 30% 10% 30%;
  }
}

@media only screen and (min-width: 1500px) {
  .card {
    margin: 0% 32% 10% 32%;
  }
}

@media only screen and (min-width: 1600px) {
  .card {
    margin: 0% 34% 10% 34%;
  }
}

@media only screen and (min-width: 1700px) {
  .card {
    margin: 0% 36% 10% 36%;
  }
}

@media only screen and (min-width: 1800px) {
  .card {
    margin: 0% 38% 5% 38%;
  }
}
</style>