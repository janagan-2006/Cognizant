import { defineStore } from 'pinia';
import { ref, computed } from 'vue';

const BASE_URL = 'https://jsonplaceholder.typicode.com';

export const useEnrollmentStore = defineStore('enrollment', () => {
  const enrolledCourses = ref([]);

  const totalCredits = computed(() =>
    enrolledCourses.value.reduce((sum, course) => sum + course.credits, 0)
  );

  function enroll(course) {
    const alreadyEnrolled = enrolledCourses.value.some((c) => c.id === course.id);
    if (!alreadyEnrolled) {
      enrolledCourses.value.push(course);
    }
  }

  function unenroll(courseId) {
    enrolledCourses.value = enrolledCourses.value.filter((c) => c.id !== courseId);
  }

  // Step 149: async action — fetches course from API then enrolls in one action
  // Components call this instead of wiring fetch + enroll separately
  async function fetchAndEnroll(courseId) {
    try {
      const response = await fetch(`${BASE_URL}/posts/${courseId}`);
      const post = await response.json();
      const course = {
        id: post.id,
        name: post.title.slice(0, 30),
        code: `CS10${post.id}`,
        credits: 3 + (post.id % 2),
        grade: 'A'
      };
      enroll(course);
    } catch (error) {
      console.error('fetchAndEnroll failed:', error.message);
    }
  }

  // Step 149: $reset clears all enrollment state back to initial
  function $reset() {
    enrolledCourses.value = [];
  }

  return {
    enrolledCourses,
    totalCredits,
    enroll,
    unenroll,
    fetchAndEnroll,
    $reset
  };
});
