from django.urls import path, include
from .views import CourseDetailView, CourseListView


app_name = 'courses'

urlpatterns = [
    path('<int:pk>', CourseDetailView.as_view(), name='detail'),
]