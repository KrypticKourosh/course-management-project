from django.urls import path
from . import views

app_name = 'enrollments'

urlpatterns = [
    path('enroll/<int:pk>/', views.EnrollView.as_view(), name='enroll'),
    path('my-courses/', views.MyCoursesView.as_view(), name='my-courses'),
    path('course/<int:course_pk>/students/', views.CourseStudentsView.as_view(), name='students'),
    path('grade/<int:pk>/', views.GradeUpdateView.as_view(), name='grade'),
]