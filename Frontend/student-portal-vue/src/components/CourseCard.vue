<template>
  <article class="course-card">
    <h3>{{ name }}</h3>
    <p>{{ code }}</p>
    <span class="credits">{{ credits }} credits</span>
    <span class="grade">Grade: {{ grade }}</span>
  </article>
</template>

<script setup>
defineProps({
  name: String,
  code: String,
  credits: Number,
  grade: String
});
</script>

<style scoped>
.course-card {
  background-color: #fff;
  border: 1px solid #d8dce2;
  border-radius: 8px;
  padding: 1.25rem;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.06);
  display: flex;
  flex-direction: column;
}

.course-card h3 {
  margin-bottom: 0.5rem;
}

.course-card .credits,
.course-card .grade {
  display: block;
  font-size: 0.85rem;
  color: #1f2a44;
  margin-top: 0.25rem;
}
</style>