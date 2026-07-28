import { createReducer, on } from '@ngrx/store';
import { loadCourses, loadCoursesSuccess, loadCoursesFailure } from './courses.actions';

export interface CoursesState {
  courses: any[];
  loading: boolean;
  error: string | null;
}

const initialState: CoursesState = {
  courses: [],
  loading: false,
  error: null
};

export const coursesReducer = createReducer(
  initialState,
  on(loadCourses, (state) => ({ ...state, loading: true, error: null })),
  on(loadCoursesSuccess, (state, { courses }) => ({ ...state, courses, loading: false })),
  on(loadCoursesFailure, (state, { error }) => ({ ...state, error, loading: false }))
);

/*
  NgRx data flow (Step 148):
  Component
    → dispatch(loadCourses())
    → Effect listens for loadCourses action
    → Effect calls CourseService.getCourses()
    → Effect dispatches loadCoursesSuccess(courses) or loadCoursesFailure(error)
    → Reducer updates state
    → Selector reads state
    → Component re-renders
*/
