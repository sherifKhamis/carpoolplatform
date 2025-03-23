import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './global.css';
import apiClient from './services/backend';

async function initializeCsrfToken() {
  try {
    await apiClient.get('/api/csrf/'); // Call the new CSRF endpoint
    console.log('CSRF token initialized');
  } catch (error) {
    console.error('Error initializing CSRF token:', error);
  }
}

initializeCsrfToken();

createApp(App).use(router).mount('#app');
