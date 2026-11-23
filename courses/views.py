from django_filters.views import FilterView
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from accounts.mixins import InstructorRequiredMixin
from .forms import CourseForm, SessionForm
from .models import Course, Session
from .filters import CourseFilter

class CourseListView(FilterView):
    model =  Course
    template_name = 'courses/course_list.html' # default = course_filter
    context_object_name = 'courses' # defualt = course_list
    filterset_class = CourseFilter

class CourseDetailView(DetailView):
    model =  Course
    # context_object_name = 'course'

class TeachingCoursesView(InstructorRequiredMixin, ListView):
    template_name = 'courses/teaching_courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.filter(instructor=self.request.user)


class CourseCreateView(InstructorRequiredMixin, CreateView):
    form_class = CourseForm
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('courses:teaching')

    def form_valid(self, form):
        form.instance.instructor = self.request.user
        return super().form_valid(form)


class CourseUpdateView(InstructorRequiredMixin, UpdateView):
    form_class = CourseForm
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('courses:teaching')

    def get_queryset(self):
        # فقط دوره‌های خود مدرس (در غیر این صورت 404)
        return Course.objects.filter(instructor=self.request.user)


class SessionCreateView(InstructorRequiredMixin, CreateView):
    form_class = SessionForm
    template_name = 'courses/session_form.html'

    def get_course(self):
        return get_object_or_404(Course, pk=self.kwargs['course_pk'], instructor=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.get_course()
        return context

    def form_valid(self, form):
        form.instance.course = self.get_course()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('courses:detail', kwargs={'pk': self.kwargs['course_pk']})