<template>
    <!-- <video id="background-video" autoplay="autoplay" loop muted poster="https://assets.codepen.io/6093409/river.jpg">
      <source src="https://assets.codepen.io/6093409/river.mp4" type="video/mp4">
    </video> -->
    <video id="background-video"
          autoplay 
          loop 
          muted
          playsinline
          poster="https://storage.googleapis.com/vuecli-profile-website/GH012245_small_cut_x8.png"  
          src="https://storage.googleapis.com/vuecli-profile-website/GH012245_small_cut_x8.mp4">
    </video>
    <!--  -->
    <!-- poster="https://assets.codepen.io/6093409/river.jpg"   -->
    
</template>

<script>

</script>

<style scoped>
    #background-video {
    width: 100vw;
    height: 100vh;
    object-fit: cover;
    position: fixed;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    z-index: -1;
    }
</style>
