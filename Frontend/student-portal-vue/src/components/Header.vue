<template>
  <header class="header">
    <div class="site-name">Student Portal</div>
    <nav>
      <ul>
        <li><RouterLink to="/">Home</RouterLink></li>
        <li><RouterLink to="/courses">Courses</RouterLink></li>
        <li><RouterLink to="/profile">Profile</RouterLink></li>
      </ul>
    </nav>
    <div class="enrolled-count">
      Enrolled: {{ store.enrolledCourses.length }}
    </div>
  </header>
</template>

<script setup>
import { useEnrollmentStore } from '../stores/enrollment';

const store = useEnrollmentStore();
</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: #1f2a44;
  color: #fff;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.site-name {
  font-size: 1.4rem;
  font-weight: bold;
}

.header nav ul {
  list-style: none;
  display: flex;
  gap: 1.5rem;
  margin: 0;
  padding: 0;
}

.header nav a {
  color: #fff;
  text-decoration: none;
}

.header nav a.router-link-active {
  text-decoration: underline;
}

.enrolled-count {
  font-size: 0.9rem;
  background-color: rgba(255, 255, 255, 0.15);
  padding: 0.35rem 0.75rem;
  border-radius: 999px;
}
</style>