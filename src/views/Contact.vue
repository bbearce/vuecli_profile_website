<template>
  <div class="container" v-bind:style="{ 'background-image': 'url(' + background_image + ')', 'background-attachment':'fixed', 'background-size':'cover', 'height':'100vh' }">
    <div class="form">
      <h1>Drop me a line:</h1>
      <form ref="form" @submit.prevent="sendEmail">
        <label>Name</label>
        <input type="text" name="user_name" v-model="name">
        <label>Email</label>
        <input type="email" name="user_email" v-model="email">
        <label>Message</label>
        <textarea name="message" v-model="message"></textarea>
        <input type="submit" value="Send">
      </form>
    </div>
  </div>
</template>

<script>
// https://www.freecodecamp.org/news/send-emails-from-your-vue-application/
// https://www.emailjs.com/docs/examples/vuejs/

// I needed both links to make this version possible
import emailjs from 'emailjs-com';

export default {
  data() {
    return {
      name: '',
      email: '',
      message: '',
      background_image: '/portfolio/some_large_landscape.jpg'
      // background_image: '/portfolio/fall_large.jpg'
      // background_image: '/portfolio/polygon_mountain.jpg'
    }
  },
  methods: {
    sendEmail() {
      emailjs.sendForm('service_kiadr3l', 'template_7solihp', this.$refs.form, 'user_Q2BTPdqD46BP10CohcjK8')
        .then((result) => {
            console.log('SUCCESS!', result.text);
            // Reset form field
            this.name = ''
            this.email = ''
            this.message = ''
        }, (error) => {
            console.log('FAILED...', error.text);
        });
    }
  }
}
</script>

<style scoped>
.container {
  padding: 80px;
}

* {box-sizing: border-box;}

.form {
  display: block;
  margin:auto;
  text-align: center;
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
  width: 50%;
}

label {
  float: left;
}

input[type=text], [type=email], textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px;
  margin-bottom: 16px;
  resize: vertical;
}

textarea {
  height: 120px;
}

input[type=submit] {
  background-color: #4CAF50;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}
</style>