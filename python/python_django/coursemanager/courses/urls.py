from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import CourseViewSet, StudentViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='course')
router.register('students', StudentViewSet, basename='student')
router.register('enrollments', EnrollmentViewSet, basename='enrollment')

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('', include(router.urls)),
]