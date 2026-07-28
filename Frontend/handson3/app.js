import { courses } from './data.js';

/* ===================== HANDS-ON 3, TASK 1: ES6+ Syntax Practice ===================== */

for (const course of courses) {
  const { name, credits } = course;
  console.log(`${name} - ${credits} credits`);
}

const formattedCourses = courses.map(
  (course) => `${course.code} — ${course.name} (${course.credits} credits)`
);
console.log(formattedCourses);

const heavyCourses = courses.filter((course) => course.credits >= 4);
console.log(`Courses with 4+ credits: ${heavyCourses.length}`);

const totalCreditsValue = courses.reduce((sum, course) => sum + course.credits, 0);
console.log(`Total credits enrolled: ${totalCreditsValue}`);

const logCourseSummary = (course) =>
  console.log(`Course: ${course.name} | Grade: ${course.grade}`);

courses.forEach(logCourseSummary);

/* ===================== HANDS-ON 3, TASK 2 & 3: Rendering + Interactivity ===================== */

const courseGrid = document.querySelector('.course-grid');
const totalCreditsEl = document.getElementById('total-credits');
const selectedCourseEl = document.getElementById('selected-course');

function renderCourses(courseList) {
  courseGrid.innerHTML = '';

  courseList.forEach((course) => {
    const card = document.createElement('article');
    card.className = 'course-card';
    card.dataset.id = course.id;
    card.setAttribute('tabindex', '0');
    card.innerHTML = `
      <h3>${course.name}</h3>
      <p>${course.code}</p>
      <span class="credits">${course.credits} credits</span>
    `;
    courseGrid.appendChild(card);
  });
}

function updateTotalCredits(courseList) {
  const total = courseList.reduce((sum, course) => sum + course.credits, 0);
  totalCreditsEl.textContent = `Total Credits: ${total}`;
}

const searchInput = document.getElementById('search-courses');
searchInput.addEventListener('input', (e) => {
  const term = e.target.value.toLowerCase();
  const filtered = courses.filter((course) => course.name.toLowerCase().includes(term));
  renderCourses(filtered);
  updateTotalCredits(filtered);
});

const sortButton = document.getElementById('sort-credits');
sortButton.addEventListener('click', () => {
  const sorted = [...courses].sort((a, b) => b.credits - a.credits);
  renderCourses(sorted);
  updateTotalCredits(sorted);
});

courseGrid.addEventListener('click', (e) => {
  const card = e.target.closest('.course-card');
  if (!card) return;
  const courseId = Number(card.dataset.id);
  const course = courses.find((c) => c.id === courseId);
  if (course) {
    selectedCourseEl.textContent = `Selected: ${course.name} — Grade: ${course.grade}`;
  }
});

courseGrid.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') {
    const card = e.target.closest('.course-card');
    if (!card) return;
    card.click();
  }
});

/* ================ HANDS-ON 4, TASK 1: Promises and async/await ================ */

// Step 45: fetchUser using .then() chaining
function fetchUser(id) {
  return fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
    .then((response) => response.json())
    .then((user) => {
      console.log(`(.then) Fetched user: ${user.name}`);
      return user;
    });
}
fetchUser(1);

// Step 46: rewritten using async/await + try/catch
async function fetchUserAsync(id) {
  try {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
    const user = await response.json();
    console.log(`(async/await) Fetched user: ${user.name}`);
    return user;
  } catch (error) {
    console.error('Error fetching user:', error.message);
  }
}
fetchUserAsync(1);

// Step 47: simulated network delay returning local course data
function fetchAllCourses() {
  return new Promise((resolve) => {
    setTimeout(() => resolve(courses), 1000);
  });
}

// Step 48: show loading message, then render after the promise resolves
async function loadCoursesWithDelay() {
  totalCreditsEl.textContent = '';
  courseGrid.innerHTML = '<p class="loading-msg">Loading courses...</p>';

  const loadedCourses = await fetchAllCourses();

  renderCourses(loadedCourses);
  updateTotalCredits(loadedCourses);
}
loadCoursesWithDelay();

// Step 49: Promise.all() - fetch two users simultaneously
async function fetchTwoUsers() {
  try {
    const [user1, user2] = await Promise.all([
      fetch('https://jsonplaceholder.typicode.com/users/1').then((res) => res.json()),
      fetch('https://jsonplaceholder.typicode.com/users/2').then((res) => res.json())
    ]);
    console.log(`Promise.all results: ${user1.name} and ${user2.name}`);
  } catch (error) {
    console.error('Error fetching users:', error.message);
  }
}
fetchTwoUsers();