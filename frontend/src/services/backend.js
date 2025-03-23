import axios from 'axios';
import Cookies from 'js-cookie';

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000', // Backend URL
  headers: {
    'X-CSRFToken': Cookies.get('csrftoken'), // Include CSRF token from cookies
    Authorization: `Bearer ${localStorage.getItem('token')}`, // Include JWT token
  },
  withCredentials: true, // Include cookies in requests
});

export default apiClient;
