import { createSlice, createAsyncThunk, createSelector } from '@reduxjs/toolkit';
import { getAllCourses } from '../api/courseApi';

// Step 143: createAsyncThunk handles the three lifecycle states
// (pending, fulfilled, rejected) automatically — no manual Promise
// management needed in the component
export const fetchAllCourses = createAsyncThunk(
  'courses/fetchAll',
  async (_, { rejectWithValue }) => {
    try {
      return await getAllCourses();
    } catch (error) {
      // rejectWithValue passes a serialisable error to the rejected action
      return rejectWithValue(error.message);
    }
  }
);

const enrollmentSlice = createSlice({
  name: 'enrollment',
  initialState: {
    enrolledCourses: [],
    courses: [],
    loading: false,
    error: null
  },
  reducers: {
    enroll(state, action) {
      const course = action.payload;
      const alreadyEnrolled = state.enrolledCourses.some((c) => c.id === course.id);
      if (!alreadyEnrolled) {
        state.enrolledCourses.push(course);
      }
    },
    unenroll(state, action) {
      const courseId = action.payload;
      state.enrolledCourses = state.enrolledCourses.filter((c) => c.id !== courseId);
    }
  },
  // Step 144: extraReducers handles the three thunk lifecycle actions
  extraReducers: (builder) => {
    builder
      .addCase(fetchAllCourses.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchAllCourses.fulfilled, (state, action) => {
        state.courses = action.payload;
        state.loading = false;
      })
      .addCase(fetchAllCourses.rejected, (state, action) => {
        state.error = action.payload;
        state.loading = false;
      });
  }
});

export const { enroll, unenroll } = enrollmentSlice.actions;
export default enrollmentSlice.reducer;

// Step 146: selectors decouple components from store shape
// If state structure changes, update only here — not every component
export const selectCourses = (state) => state.enrollment.courses;
export const selectCoursesLoading = (state) => state.enrollment.loading;
export const selectCoursesError = (state) => state.enrollment.error;
export const selectEnrolledCourses = (state) => state.enrollment.enrolledCourses;

// Memoised derived selector using createSelector
export const selectEnrolledCount = createSelector(
  selectEnrolledCourses,
  (enrolled) => enrolled.length
);

export const selectTotalCredits = createSelector(
  selectEnrolledCourses,
  (enrolled) => enrolled.reduce((sum, c) => sum + c.credits, 0)
);
