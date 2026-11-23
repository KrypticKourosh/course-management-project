from django.views.generic import DetailView
from django_filters.views import FilterView

from .models import Course
from .filters import CourseFilter

class CourseListView(FilterView):
    model =  Course
    template_name = 'courses/course_list.html' # default = course_filter
    context_object_name = 'courses' # defualt = course_list
    filterset_class = CourseFilter

class CourseDetailView(DetailView):
    model =  Course
    # context_object_name = 'course'