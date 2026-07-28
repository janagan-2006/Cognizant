import { defineStore } from 'pinia';
import { ref, computed } from 'vue';

export const useEnrollmentStore = defineStore('enrollment', () => {
  // state
  const enrolledCourses = ref([]);

  // computed
  const totalCredits = computed(() =>
    enrolledCourses.value.reduce((sum, course) => sum + course.credits, 0)
  );

  // actions
  function enroll(course) {
    const alreadyEnrolled = enrolledCourses.value.some((c) => c.id === course.id);
    if (!alreadyEnrolled) {
      enrolledCourses.value.push(course);
    }
  }

  function unenroll(courseId) {
    enrolledCourses.value = enrolledCourses.value.filter((c) => c.id !== courseId);
  }

  return { enrolledCourses, totalCredits, enroll, unenroll };
});