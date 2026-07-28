import { createAction } from '@ngrx/store';

export const loadCourses = createAction('[Courses] Load Courses');
export const loadCoursesSuccess = createAction(
  '[Courses] Load Courses Success',
  (courses: any[]) => ({ courses })
);
export const loadCoursesFailure = createAction(
  '[Courses] Load Courses Failure',
  (error: string) => ({ error })
);
