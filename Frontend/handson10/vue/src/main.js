import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router';

const app = createApp(App);

// Step 150: global error handler — catches any unhandled error
// thrown during component rendering, watchers, or lifecycle hooks.
// Shows a fallback rather than a blank screen.
app.config.errorHandler = (error, instance, info) => {
  console.error('[Vue errorHandler]', error, info);
  const container = document.getElementById('app');
  if (container) {
    container.innerHTML = `
      <div style="padding:3rem;text-align:center;">
        <h2 style="color:#b3261e">Something went wrong</h2>
        <p style="color:#555;margin-top:1rem">${error.message}</p>
        <button onclick="location.reload()"
          style="margin-top:1.5rem;padding:0.6rem 1.2rem;background:#1f2a44;
                 color:#fff;border:none;border-radius:6px;cursor:pointer">
          Reload Page
        </button>
      </div>
    `;
  }
};

app.use(createPinia());
app.use(router);
app.mount('#app');
