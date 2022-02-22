import { createApp } from 'vue'
import App from './App.vue'
import { createWebHistory, createRouter } from "vue-router";

// Components
import HelloWorld from '@/components/HelloWorld.vue' // demo from vue cli
// Views
import PageNotFound from '@/views/PageNotFound.vue'
// import Resume from '@/views/Resume.vue' // TBD
import Contact from '@/views/Contact.vue'
import Portfolio from '@/views/Portfolio.vue'
import Blog_List from '@/views/Blog_List.vue'
import Blog from '@/components/Blog.vue'


const routes = [
    {
      path: "/main_site/hello", name: "Hello", component: HelloWorld
    },
    // TBD
    // {
    //   path: "/main_site/resume", name: "Resume", component: Resume
    // },
    {
      path: "/main_site/contact", name: "Contact", component: Contact
    },
    {
      path: "/main_site/portfolio", name: "Portfolio", component: Portfolio
    },
    {
      path: "/main_site/blog_list", name: "Blog_List", component: Blog_List
    },
    {
      path: "/main_site/blog_post/:date", name: "Blog_Post", component: Blog
    },
    {
      path: '/:catchAll(.*)*',
      name: "PageNotFound",
      component: PageNotFound,
    },
  ];

const router = createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHistory(),
    routes, // short for `routes: routes`

  })


const app = createApp(App)
app.use(router)
app.mount('#app')

