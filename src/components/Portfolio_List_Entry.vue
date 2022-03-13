<template>
  <div class="container">
    <!-- https://codepen.io/jacklegge/pen/EMdXQm -->
    <div class="row">
      <div class="col-md-4">
        <div class="card">
          <a v-bind:href="this.link" target="_blank">
            <img
              class="card-img-top portfolio-card__image"
              v-bind:src="'/portfolio/' + this.image"
              alt="Card image cap"
            />
          </a>
          <div class="card-body">
            <h6
              class="
                card-subtitle
                mb-2
                portfolio-card__category portfolio-card__category__retail
              "
            >
              {{ date }}
            </h6>
            <h4 class="card-title mb-2 portfolio-card__title">{{ title }}</h4>
            <p class="card-text portfolio-card__text">{{ desc }}</p>
            <p>
              <a
                class="portfolio-card__a"
                v-bind:href="this.link"
                target="_blank"
              >
                <span
                  class="portfolio-card__stage portfolio-card__stage__complete"
                >
                  <i class="fas fa-building portfolio-card__stage__icon"> </i
                  >Check It Out
                </span>
              </a>
            </p>
            <a
              v-bind:href="this.github"
              class="card-link portfolio-card__link"
              target="_blank"
              >Github</a
            >
            <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// https://www.w3schools.com/howto/howto_css_blog_layout.asp
export default {
  name: "blog_list_entry",
  components: {},
  props: {
    id: Number,
    title: String,
    desc: String,
    author: String,
    date: String,
    image: String,
    link: String,
    github: String,
  },
  created() {},
  data() {
    return {};
  },
};
</script>

<style scoped>
.portfolio-card__a {
  /* BB*/
  text-decoration: none;
}

.card {
  margin: 2rem 10rem 2rem 10rem;
  border: none;
  border-radius: 0px;
  background-color: #f1f3f4;
  box-shadow: -2px 1px 8px 1px lightgrey;
}

@media only screen and (max-width: 700px) {
  .card {
    margin: 1rem 5rem 1rem 5rem;
  }
}

.portfolio-card__image {
  width: 70%;
  max-height: 15rem;
  margin: 5%;
}

@media only screen and (min-width: 700px) {
  .portfolio-card__image {
    width: 70%;
    max-height: 60rem;
  }

}

@media only screen and (min-width: 1300px) {
  .card {
    margin: 2rem 15rem 2rem 15rem;
  }
}


.portfolio-card__title {
  font-family: "Barlow Condensed", sans-serif;
  font-size: 2rem;
  text-transform: uppercase;
}

.portfolio-card__category {
  font-family: "Barlow Condensed", sans-serif;
  font-size: 1rem;
  text-transform: uppercase;
}

.portfolio-card__category__offices {
  color: red;
}

.portfolio-card__category__industrial {
  color: blue;
}

.portfolio-card__category__retail {
  color: green;
}

.portfolio-card__text {
  font-family: "Abel", sans-serif;
  font-size: 1rem;
}

.portfolio-card__stage {
  color: white;
  text-transform: uppercase;
  padding: 6px;
  font-family: "Barlow Condensed", sans-serif;
}

.portfolio-card__stage__icon {
  margin-right: 5px;
}

.portfolio-card__stage__complete {
  background-color: green;
}

.portfolio-card__stage__construction {
  background-color: red;
}

.portfolio-card__stage__planning {
  background-color: lightblue;
}

.portfolio-card__link {
  font-family: "Barlow Condensed", sans-serif;
  text-transform: uppercase;
  font-size: 0.8rem;
  color: grey;
  text-decoration: underline;
  transition: 0.3s;
}

.portfolio-card__link:hover {
  color: black;
}
</style>