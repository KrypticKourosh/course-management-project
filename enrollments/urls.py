from django.urls import path
from .views import EnrollView, MyCoursesView


app_name = 'enrollments'

urlpatterns = [
    path('enroll/<int:pk>/', EnrollView.as_view(), name='enroll'),
    path('my-courses/', MyCoursesView.as_view(), name='my-courses'),
]