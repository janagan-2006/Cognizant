import { Component, OnInit } from '@angular/core';
import { CourseService, Course } from '../course.service';

@Component({
  selector: 'app-course-list',
  standalone: false,
  templateUrl: './course-list.component.html',
  styleUrls: ['./course-list.component.css']
})
export class CourseListComponent implements OnInit {
  courses: Course[] = [];
  searchTerm = '';
  loading = false;
  error = '';

  constructor(private courseService: CourseService) {}

  ngOnInit(): void {
    this.loading = true;
    this.courseService.getCourses().subscribe({
      next: (data) => {
        this.courses = data;
        this.loading = false;
      },
      error: () => {
        this.error = 'Failed to load courses.';
        this.loading = false;
      }
    });
  }

  get filteredCourses(): Course[] {
    return this.courses.filter((course) =>
      course.name.toLowerCase().includes(this.searchTerm.toLowerCase())
    );
  }
}
