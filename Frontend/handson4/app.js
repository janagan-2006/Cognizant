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

function fetchUser(id) {
  return fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
    .then((response) => response.json())
    .then((user) => {
      console.log(`(.then) Fetched user: ${user.name}`);
      return user;
    });
}
fetchUser(1);

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

function fetchAllCourses() {
  return new Promise((resolve) => {
    setTimeout(() => resolve(courses), 1000);
  });
}

async function loadCoursesWithDelay() {
  totalCreditsEl.textContent = '';
  courseGrid.innerHTML = '<p class="loading-msg">Loading courses...</p>';

  const loadedCourses = await fetchAllCourses();

  renderCourses(loadedCourses);
  updateTotalCredits(loadedCourses);
}
loadCoursesWithDelay();

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

/* ================ HANDS-ON 4, TASK 2: Fetch API with Error Handling ================ */

const BASE_URL = 'https://jsonplaceholder.typicode.com';

async function apiFetch(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Request failed: ${response.status} ${response.statusText}`);
  }
  return response.json();
}

const notificationsList = document.getElementById('notifications-list');

function renderNotifications(posts) {
  notificationsList.innerHTML = '';
  posts.slice(0, 5).forEach((post) => {
    const card = document.createElement('div');
    card.className = 'notification-card';
    card.innerHTML = `
      <h4>${post.title}</h4>
      <p>${post.body}</p>
    `;
    notificationsList.appendChild(card);
  });
}

async function loadNotifications() {
  notificationsList.innerHTML = '<div class="spinner"></div>';

  try {
    const posts = await apiFetch(`${BASE_URL}/posts`);
    renderNotifications(posts);
  } catch (error) {
    notificationsList.innerHTML = `
      <p class="error-msg">Couldn't load notifications. Please try again.</p>
      <button type="button" id="retry-notifications">Retry</button>
    `;
    document
      .getElementById('retry-notifications')
      .addEventListener('click', loadNotifications);
  }
}
loadNotifications();

const errorDemoResult = document.getElementById('error-demo-result');
const triggerErrorBtn = document.getElementById('trigger-error');

async function loadBrokenEndpoint() {
  errorDemoResult.innerHTML = '<div class="spinner"></div>';

  try {
    const data = await apiFetch(`${BASE_URL}/nonexistent`);
    errorDemoResult.textContent = JSON.stringify(data);
  } catch (error) {
    errorDemoResult.innerHTML = `
      <p class="error-msg">Something went wrong: ${error.message}</p>
      <button type="button" id="retry-error-demo">Retry</button>
    `;
    document
      .getElementById('retry-error-demo')
      .addEventListener('click', loadBrokenEndpoint);
  }
}

triggerErrorBtn.addEventListener('click', loadBrokenEndpoint);

/* ================ HANDS-ON 4, TASK 3: Introduction to Axios ================ */

// Step 56: apiFetch rewritten with Axios
// Axios automatically parses JSON and throws on non-2xx responses,
// so there's no manual response.ok check needed (unlike fetch).
async function apiFetchAxios(url, config = {}) {
  const response = await axios.get(url, config);
  return response.data;
}

// Step 58: request interceptor - logs every outgoing request
axios.interceptors.request.use((config) => {
  console.log(`API call started: ${config.url}`);
  return config;
});

// Step 57: axios.get with a params object - posts belonging to user 1
const loadAxiosPostsBtn = document.getElementById('load-axios-posts');
const axiosPostsResult = document.getElementById('axios-posts-result');

async function loadUserOnePosts() {
  axiosPostsResult.innerHTML = '<div class="spinner"></div>';

  try {
    const posts = await apiFetchAxios(`${BASE_URL}/posts`, {
      params: { userId: 1 }
    });

    axiosPostsResult.innerHTML = '';
    posts.forEach((post) => {
      const card = document.createElement('div');
      card.className = 'notification-card';
      card.innerHTML = `<h4>${post.title}</h4>`;
      axiosPostsResult.appendChild(card);
    });
  } catch (error) {
    axiosPostsResult.innerHTML = `<p class="error-msg">Failed to load posts: ${error.message}</p>`;
  }
}

loadAxiosPostsBtn.addEventListener('click', loadUserOnePosts);

// Step 59: fetch vs axios — three key differences
// 1. Parsing: fetch requires a manual .json() call; axios parses JSON automatically into response.data.
// 2. Error handling: fetch only rejects on network failure (you must check response.ok yourself for
//    HTTP errors like 404/500); axios rejects automatically on any non-2xx status.
// 3. Config: axios accepts a single config object for params, headers, and timeout directly in the
//    call (e.g. axios.get(url, { params, timeout: 5000 })); fetch needs the query string built manually
//    and timeouts handled via AbortController.