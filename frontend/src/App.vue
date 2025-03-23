<template>
  <RouterView></RouterView>
  <footer>Developed and designed by Sherif Khamis</footer>
</template>

<script>
import { RouterView } from 'vue-router';

export default {
  name: 'App',
  components: {
    RouterView
  }
}
</script>

<style>
html, body {
  margin: 0;
  height: 100%;
  width: 100%;
  background-color: #F8EDE3;
  color: #798777;
}

/* Center content within the wrapper only */
.wrapper {
  display: flex;
  text-align: center;
  min-height: calc(100vh - 60px); /* Adjust based on footer height */
  flex-direction: column;
}

/* Footer styling */
footer {
  background-color: #798777;
  color: #F8EDE3;
  padding: 20px 0;
  width: 100%;
  margin: 0;
  text-align: center;
  position: relative; /* or fixed if you want it always at the bottom */
}

Button {
  background-color: #798777;
  color: #F8EDE3;
  font-size: 20px;
  padding: 10px;
  margin: 30px;
  border-color: #798777;
  border-radius: 10px;
}
</style>
