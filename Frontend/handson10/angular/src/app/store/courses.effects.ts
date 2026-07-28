import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { switchMap, map, catchError, of } from 'rxjs';
import { CourseService } from '../course.service';
import { loadCourses, loadCoursesSuccess, loadCoursesFailure } from './courses.actions';

@Injectable()
export class CoursesEffects {
  loadCourses$ = createEffect(() =>
    this.actions$.pipe(
      ofType(loadCourses),
      switchMap(() =>
        this.courseService.getCourses().pipe(
          map((courses) => loadCoursesSuccess(courses)),
          catchError((err) => of(loadCoursesFailure(err.message)))
        )
      )
    )
  );

  constructor(private actions$: Actions, private courseService: CourseService) {}
}
