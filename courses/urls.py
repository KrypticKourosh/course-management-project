from django.urls import path
from . import views


app_name = 'courses'

urlpatterns = [
    path('teaching/', views.TeachingCoursesView.as_view(), name='teaching'),
    path('create/', views.CourseCreateView.as_view(), name='create'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.CourseUpdateView.as_view(), name='edit'),
    path('<int:course_pk>/sessions/add/', views.SessionCreateView.as_view(), name='session-add'),
]