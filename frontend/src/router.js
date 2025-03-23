import { createRouter, createWebHistory } from 'vue-router';
import UserLogin from './components/UserLogin.vue';
import DriverRegistration from './components/DriverRegistration.vue';

const routes = [
  { path: '/', component: UserLogin },
  { path: '/driver-registration', component: DriverRegistration },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
