import axios from 'axios';

// Step 138: single configured Axios instance — one place to change
// baseURL, headers, timeout, and interceptors for the entire app
const apiClient = axios.create({
  baseURL: 'https://jsonplaceholder.typicode.com',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Step 141: request interceptor — attaches mock auth token to every request
apiClient.interceptors.request.use((config) => {
  config.headers['Authorization'] = 'Bearer mock-token-abc123';
  console.log(`[API] ${config.method.toUpperCase()} ${config.baseURL}${config.url}`);
  return config;
});

// Step 140: response interceptor
// (a) unwraps response.data so callers receive data directly
// (b) catches errors and throws a standardised Error object
apiClient.interceptors.response.use(
  (response) => response.data,
  (error) => {
    const message = error.response
      ? `Request failed: ${error.response.status} ${error.response.statusText}`
      : 'Network error — please check your connection';
    const statusCode = error.response?.status ?? 0;
    const standardError = new Error(message);
    standardError.statusCode = statusCode;
    throw standardError;
  }
);

export default apiClient;
