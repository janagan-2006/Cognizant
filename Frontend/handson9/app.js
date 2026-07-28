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
const resultsCountEl = document.getElementById('search-results-count');

/*
  Step 129: cards are rendered with tabindex="0" and role="listitem"
  so they are reachable via Tab and announced correctly within role="list"
  on the grid container.
  Step 132: verified Tab order — cards are in DOM order which matches
  visual order, so no mismatch between visual and keyboard navigation.
*/
function renderCourses(courseList) {
  courseGrid.innerHTML = '';

  courseList.forEach((course) => {
    const card = document.createElement('article');
    card.className = 'course-card';
    card.dataset.id = course.id;
    card.setAttribute('tabindex', '0');
    card.setAttribute('role', 'listitem');
    card.setAttribute(
      'aria-label',
      `${course.name}, ${course.code}, ${course.credits} credits, Grade: ${course.grade}. Press Enter to select.`
    );

    card.innerHTML = `
      <h3>${course.name}</h3>
      <p>${course.code}</p>
      <span class="credits">${course.credits} credits</span>
    `;
    courseGrid.appendChild(card);
  });

  /*
    Step 130: update the aria-live="polite" region after every render.
    Screen readers will announce the new count once the current
    speech finishes — without interrupting what's being read.
  */
  resultsCountEl.textContent =
    courseList.length === 0
      ? 'No courses found'
      : `${courseList.length} course${courseList.length === 1 ? '' : 's'} found`;
}

function updateTotalCredits(courseList) {
  const total = courseList.reduce((sum, course) => sum + course.credits, 0);
  totalCreditsEl.textContent = `Total Credits: ${total}`;
}

renderCourses(courses);
updateTotalCredits(courses);

/* Step 132: Tab order verification
   Keyboard navigation test sequence:
   1. Tab → focuses hamburger button (mobile) or first nav link (desktop)
   2. Tab × 4 → cycles through all 4 nav links
   3. Tab → focuses search input
   4. Tab → focuses Sort by Credits button
   5. Tab × 5 → cycles through all 5 course cards
   Result: all interactive elements reachable in logical DOM order.
   No focus traps detected. No elements skipped. ✓
*/

const searchInput = document.getElementById('search-courses');
searchInput.addEventListener('input', (e) => {
  const term = e.target.value.toLowerCase();
  const filtered = courses.filter((course) =>
    course.name.toLowerCase().includes(term)
  );
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
    selectedCourseEl.textContent =
      `Selected: ${course.name} — Grade: ${course.grade}`;
  }
});

/*
  Step 129: Enter or Space on a focused card triggers the same
  action as a click. Space is included because role="button" elements
  are conventionally activated by both Enter and Space.
  e.preventDefault() on Space prevents the page from scrolling.
*/
courseGrid.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' || e.key === ' ') {
    e.preventDefault();
    const card = e.target.closest('.course-card');
    if (!card) return;
    card.click();
  }
});

/*
  Step 131: aria-expanded toggles true/false on the hamburger button
  when the mobile nav opens and closes.
  Screen readers announce "Open navigation menu, collapsed/expanded"
  so users know the current state of the control.
*/
const hamburgerBtn = document.getElementById('hamburger-btn');
const mainNav = document.getElementById('main-nav');

hamburgerBtn.addEventListener('click', () => {
  const isExpanded = hamburgerBtn.getAttribute('aria-expanded') === 'true';
  hamburgerBtn.setAttribute('aria-expanded', String(!isExpanded));
  mainNav.classList.toggle('nav-open');

  // Update aria-label to reflect new state
  hamburgerBtn.setAttribute(
    'aria-label',
    isExpanded ? 'Open navigation menu' : 'Close navigation menu'
  );
});

/*
  Step 128: update aria-current="page" dynamically when a nav
  link is clicked — removes it from all links first, then adds
  it to the clicked one so only one link is marked active at a time.
*/
const navLinks = document.querySelectorAll('nav a');
navLinks.forEach((link) => {
  link.addEventListener('click', () => {
    navLinks.forEach((l) => l.removeAttribute('aria-current'));
    link.setAttribute('aria-current', 'page');
  });
});

/*
  Step 137: initialise css-vars-ponyfill for older browser support.
  This runs after the DOM is ready, reads all CSS custom properties,
  and re-applies them as static values for browsers that don't
  support CSS variables natively (e.g. IE11).
  Simulated in DevTools via User Agent override → IE11 mode.
*/
if (typeof cssVars !== 'undefined') {
  cssVars({
    onlyLegacy: true // only runs in browsers that lack CSS variable support
  });
}
