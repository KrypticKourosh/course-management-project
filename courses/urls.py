from django.urls import path
from .views import CourseDetailView


app_name = 'courses'

urlpatterns = [
    path('<int:pk>', CourseDetailView.as_view(), name='detail'),
]