<template>
  <div class="wrapper">
    <h1> Welcome to the Carpool Platform</h1>
    <img src="../assets/basicCar.png" alt="Basic Green Car" style="width: 1000px; height: auto; display: block; margin: 0 auto;">
    <div>
      <h2>Are you a driver or a passenger ?</h2>
      <button @click="goToDriverRegistration">Driver</button>
      <button>Passenger</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserLogin',
  methods: {
    goToDriverRegistration() {
      // Navigiere zur DriverRegistration-Seite
      this.$router.push('/driver-registration');
    },
  },
};
</script>

<style>

</style>