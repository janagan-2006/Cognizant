<template>
  <Header />
  <main>
    <RouterView />
  </main>
  <footer class="footer">
    <p>&copy; 2026 Student Portal. All rights reserved.</p>
  </footer>
</template>

<script setup>
import Header from './components/Header.vue';
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, Helvetica, sans-serif;
  background-color: #f4f6f8;
  color: #222;
}

.footer {
  text-align: center;
  padding: 1rem;
  background-color: #1f2a44;
  color: #fff;
  font-size: 0.85rem;
}
</style>
