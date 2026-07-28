<template>
  <section class="course-detail">
    <p v-if="loading" class="status-msg">Loading course details...</p>

    <template v-else-if="course">
      <h2>{{ course.name }}</h2>
      <p class="code">{{ course.code }}</p>
      <p>{{ course.description }}</p>
      <p><strong>Credits:</strong> {{ course.credits }}</p>
      <p><strong>Grade:</strong> {{ course.grade }}</p>
      <button type="button" @click="handleEnroll">
        Enroll &amp; Go to Profile
      </button>
    </template>

    <p v-else class="status-msg error-msg">Course not found.</p>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useEnrollmentStore } from '../stores/enrollment';

const route = useRoute();
const router = useRouter();
const store = useEnrollmentStore();

const course = ref(null);
const loading = ref(true);

onMounted(async () => {
  const id = route.params.id;
  const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`);
  const post = await response.json();

  course.value = {
    id: post.id,
    name: post.title,
    code: `CS10${post.id}`,
    credits: 3 + (post.id % 2),
    grade: 'A',
    description: post.body
  };

  loading.value = false;
});

// Step 115: programmatic navigation to /profile after enrolling
function handleEnroll() {
  store.enroll(course.value);
  router.push('/profile');
}
</script>

<style scoped>
.course-detail {
  padding: 2rem 1.5rem;
  max-width: 600px;
}

.course-detail h2 {
  margin-bottom: 0.5rem;
}

.course-detail .code {
  color: #555;
  margin-bottom: 1rem;
}

.course-detail p {
  margin-bottom: 0.5rem;
}

.course-detail button {
  margin-top: 1rem;
  padding: 0.6rem 1.2rem;
  border: 2px solid #1f2a44;
  border-radius: 6px;
  background-color: #1f2a44;
  color: #fff;
  cursor: pointer;
}

.status-msg {
  padding: 1rem 1.5rem;
  color: #555;
  font-style: italic;
}

.error-msg {
  color: #b3261e;
  font-style: normal;
}
</style>