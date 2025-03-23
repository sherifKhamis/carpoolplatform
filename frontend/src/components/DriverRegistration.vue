<template>
    <div class="wrapper">
      <h1>Driver & Car Registration</h1>
      <form @submit.prevent="submitForm">
        <h2 style="color: black;">Enter your Driver Details:</h2>
        <div class="formDiv">
          <label for="license_number">License Number:</label>
          <input
            type="text"
            id="license_number"
            v-model="form.license_number"
            placeholder="Enter your license number"
            required
          />
        </div>
        <div class="formDiv">
          <label for="vehicle_model">Vehicle Model:</label>
          <input
            type="text"
            id="vehicle_model"
            v-model="form.vehicle_model"
            placeholder="Enter your vehicle model"
            required
          />
        </div>
        <div class="formDiv">
          <label for="seats_available">Seats Available:</label>
          <input
            type="number"
            id="seats_available"
            v-model.number="form.seats_available"
            min="0"
            placeholder="Enter number of available seats"
            required
          />
        </div>
  
        <h2 style="color: black;">Enter your Car Specifications:</h2>
        <div class="formDiv">
          <label for="make">Car Manufacturer:</label>
          <input
            type="text"
            id="make"
            v-model="form.make"
            placeholder="Enter car manufacturer"
            required
          />
        </div>
        <div class="formDiv">
          <label for="model">Car Model:</label>
          <input
            type="text"
            id="model"
            v-model="form.model"
            placeholder="Enter car model"
            required
          />
        </div>
        <div class="formDiv">
          <label for="year">Year of Manufacture:</label>
          <input
            type="number"
            id="year"
            v-model.number="form.year"
            placeholder="Enter year of manufacture"
            required
          />
        </div>
        <div class="formDiv">
          <label for="color">Car Color:</label>
          <input
            type="text"
            id="color"
            v-model="form.color"
            placeholder="Enter car color"
          />
        </div>
        <div class="formDiv">
          <label for="license_plate">License Plate:</label>
          <input
            type="text"
            id="license_plate"
            v-model="form.license_plate"
            placeholder="Enter license plate"
            required
          />
        </div>
        <div class="formDiv">
          <label for="seats">Total Seats in Car:</label>
          <input
            type="number"
            id="seats"
            v-model.number="form.seats"
            min="1"
            placeholder="Enter total number of seats"
            required
          />
        </div>
        <button class="formButton" type="submit">Submit</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: "DriverRegistration",
    data() {
      return {
        form: {
          // DriverProfile fields
          license_number: "",
          vehicle_model: "",
          seats_available: 0,
          // Car fields
          make: "",
          model: "",
          year: null,
          color: "",
          license_plate: "",
          seats: 0,
        },
      };
    },
    methods: {
      async submitForm() {
        try {
          const response = await axios.post('http://127.0.0.1:8000/api/register-driver/', this.form);
          alert(response.data.message);
        } catch (error) {
          console.error('Error submitting form:', error);
          alert('Failed to register driver.');
        }
      }
    }
  };
  </script>
  
  <style>
  
  </style>