<template>
  <section class="profile-section">
    <h2>Student Profile</h2>
    <div class="profile-form">
      <label>
        Name
        <input type="text" v-model="profileName" placeholder="Your name" />
      </label>
      <label>
        Email
        <input type="email" v-model="profileEmail" placeholder="you@example.com" />
      </label>
      <label>
        Semester
        <input type="number" v-model="profileSemester" placeholder="e.g. 6" min="1" max="8" />
      </label>
    </div>

    <div class="enrolled-list">
      <h3>My Enrolled Courses</h3>

      <p v-if="enrolledCourses.length === 0" class="status-msg">
        No courses enrolled yet.
      </p>

      <ul v-else>
        <li v-for="course in enrolledCourses" :key="course.id">
          <span>{{ course.name }} — {{ course.credits }} credits</span>
          <button
            type="button"
            class="remove-btn"
            @click="unenroll(course.id)"
          >
            Remove
          </button>
        </li>
      </ul>

      <p v-if="enrolledCourses.length > 0" class="total-credits">
        Total Credits: {{ totalCredits }}
      </p>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';
import { storeToRefs } from 'pinia';
import { useEnrollmentStore } from '../stores/enrollment';

// Step 149: storeToRefs extracts reactive refs from the store
// without losing reactivity — plain destructuring would break it
const store = useEnrollmentStore();
const { enrolledCourses, totalCredits } = storeToRefs(store);
const { unenroll } = store;

const profileName = ref('');
const profileEmail = ref('');
const profileSemester = ref('');
</script>

<style scoped>
.profile-section {
  padding: 2rem 1.5rem;
  background-color: #eef1f6;
  min-height: 60vh;
}

.profile-section h2 {
  margin-bottom: 1.5rem;
}

.profile-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-width: 400px;
  margin-bottom: 2rem;
}

.profile-form label {
  display: flex;
  flex-direction: column;
  font-size: 0.9rem;
  font-weight: bold;
  gap: 0.35rem;
}

.profile-form input {
  padding: 0.6rem 0.8rem;
  border: 1px solid #c5cdd9;
  border-radius: 6px;
  font-size: 0.95rem;
  font-weight: normal;
  background-color: #fff;
}

.enrolled-list {
  max-width: 500px;
}

.enrolled-list h3 {
  margin-bottom: 1rem;
}

.enrolled-list ul {
  list-style: none;
}

.enrolled-list li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #fff;
  border: 1px solid #d8dce2;
  border-radius: 6px;
  padding: 0.75rem 1rem;
  margin-bottom: 0.5rem;
}

.remove-btn {
  padding: 0.35rem 0.8rem;
  border: 1px solid #b3261e;
  border-radius: 6px;
  background-color: transparent;
  color: #b3261e;
  cursor: pointer;
  font-size: 0.8rem;
}

.remove-btn:hover {
  background-color: #b3261e;
  color: #fff;
}

.total-credits {
  margin-top: 1rem;
  font-weight: bold;
  color: #1f2a44;
}

.status-msg {
  color: #555;
  font-style: italic;
}
</style>
