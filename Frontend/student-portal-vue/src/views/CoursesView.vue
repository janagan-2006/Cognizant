<template>
  <section id="courses">
    <h2>Enrolled Courses</h2>

    <input
      type="text"
      placeholder="Search courses..."
      v-model="searchTerm"
      class="search-input"
    />

    <p v-if="filteredCourses.length === 0" class="status-msg">No courses found</p>

    <div class="course-grid">
      <div v-for="course in filteredCourses" :key="course.id" class="card-wrapper">
        <RouterLink :to="`/courses/${course.id}`" class="card-link">
          <CourseCard
            :name="course.name"
            :code="course.code"
            :credits="course.credits"
            :grade="course.grade"
          />
        </RouterLink>
        <button
          type="button"
          class="enroll-btn"
          @click="store.enroll(course)"
        >
          Enroll
        </button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import CourseCard from '../components/CourseCard.vue';
import { useEnrollmentStore } from '../stores/enrollment';

const store = useEnrollmentStore();

const courses = ref([]);
const searchTerm = ref('');

onMounted(() => {
  courses.value = [
    { id: 1, name: 'Data Structures', code: 'CS101', credits: 4, grade: 'A' },
    { id: 2, name: 'Database Management Systems', code: 'CS102', credits: 3, grade: 'B+' },
    { id: 3, name: 'Web Development', code: 'CS103', credits: 4, grade: 'A-' },
    { id: 4, name: 'Operating Systems', code: 'CS104', credits: 3, grade: 'B' },
    { id: 5, name: 'Computer Networks', code: 'CS105', credits: 4, grade: 'A' }
  ];
});

const filteredCourses = computed(() =>
  courses.value.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase())
  )
);
</script>

<style scoped>
#courses {
  padding: 2rem 1.5rem;
}

.search-input {
  display: block;
  width: 100%;
  max-width: 400px;
  padding: 0.6rem 0.8rem;
  margin-bottom: 1.5rem;
  border: 1px solid #c5cdd9;
  border-radius: 6px;
  font-size: 0.95rem;
}

.status-msg {
  padding: 1rem 0;
  color: #555;
  font-style: italic;
}

.course-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.25rem;
}

.card-wrapper {
  display: flex;
  flex-direction: column;
}

.card-link {
  text-decoration: none;
  color: inherit;
  display: block;
}

.enroll-btn {
  margin-top: 0.5rem;
  padding: 0.5rem;
  border: 2px solid #1f2a44;
  border-radius: 6px;
  background-color: #1f2a44;
  color: #fff;
  cursor: pointer;
}

.enroll-btn:hover {
  background-color: #14213a;
}
</style>