import apiClient from './apiClient';

// Step 139: all course-related API calls in one place
// Components never call axios or fetch directly

export async function getAllCourses() {
  const posts = await apiClient.get('/posts?_limit=5');
  return posts.map((post, index) => ({
    id: post.id,
    name: post.title.slice(0, 30),
    code: `CS10${index + 1}`,
    credits: 3 + (index % 2),
    grade: ['A', 'B+', 'A-', 'B', 'A'][index % 5]
  }));
}

export async function getCourseById(id) {
  const post = await apiClient.get(`/posts/${id}`);
  return {
    id: post.id,
    name: post.title,
    code: `CS10${post.id}`,
    credits: 3 + (post.id % 2),
    grade: 'A',
    description: post.body
  };
}

export async function enrollStudent(studentId, courseId) {
  // JSONPlaceholder simulates a POST — returns the posted data
  const result = await apiClient.post('/posts', {
    studentId,
    courseId,
    enrolledAt: new Date().toISOString()
  });
  return result;
}
