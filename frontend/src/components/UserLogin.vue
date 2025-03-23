<template>
  <div class="wrapper">
    <h1> Welcome to the Carpool Platform</h1>
    <img src="../assets/basicCar.png" alt="Basic Green Car" style="width: 1000px; height: auto; display: block; margin: 0 auto;">
    <div>
      <h2>Are you a driver or a passenger ?</h2>
      <Button @click="handleDriverClick">Driver</Button>
      <Button>Passenger</Button>
    </div>
  </div>
</template>

<script>
import apiClient from '../services/backend';

export default {
  name: 'UserLogin',
  methods: {
    async handleDriverClick() {
      try {
        // Call the backend API to update the user's role to 'driver'
        const response = await apiClient.post('/api/update-role/');
        console.log(response.data.message);

        // Navigate to the DriverRegistration page
        this.$router.push('/DriverRegistration');
      } catch (error) {
        console.error("Error updating role:", error.response?.data || error.message);
        alert("Failed to update role. Please try again.");
      }
    }
  }
}
</script>

<style>

</style>