<template>
  <section class="hero">
    <h1>Welcome to the Student Portal</h1>
    <p>Track your courses, grades, and notifications all in one place.</p>
    <RouterLink to="/courses">
      <button type="button">Explore Courses</button>
    </RouterLink>
  </section>
</template>

<script setup>
</script>

<style scoped>
.hero {
  text-align: center;
  padding: 4rem 1.5rem;
  background-color: #e8edf5;
  min-height: 40vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}

.hero h1 {
  font-size: 2rem;
}

.hero p {
  color: #444;
}

.hero button {
  padding: 0.75rem 1.5rem;
  border: 2px solid #1f2a44;
  border-radius: 6px;
  background-color: #1f2a44;
  color: #fff;
  cursor: pointer;
  font-size: 1rem;
}
</style>