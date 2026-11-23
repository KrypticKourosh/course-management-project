from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, UpdateView
from django.urls import reverse

from accounts.mixins import InstructorRequiredMixin

from .forms import GradeForm

from accounts.models import User
from courses.models import Course

from .models import Enrollment


class EnrollView(LoginRequiredMixin, View):
    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)

        # فقط دانشجو می‌تواند ثبت‌نام کند
        if request.user.role != User.Role.STUDENT:
            messages.error(request, 'فقط دانشجویان می‌توانند ثبت‌نام کنند.')
            return redirect('courses:detail', pk=pk)

        # ثبت‌نام تکراری
        if Enrollment.objects.filter(student=request.user, course=course).exists():
            messages.error(request, 'شما قبلاً در این دوره ثبت‌نام کرده‌اید.')
            return redirect('courses:detail', pk=pk)

        # ظرفیت دوره
        if course.enrollments.count() >= course.capacity: # type: ignore
            messages.error(request, 'ظرفیت این دوره تکمیل شده است.')
            return redirect('courses:detail', pk=pk)

        Enrollment.objects.create(student=request.user, course=course)
        messages.success(request, 'ثبت‌نام شما با موفقیت انجام شد.')
        return redirect('enrollments:my-courses')


class MyCoursesView(LoginRequiredMixin, ListView):
    template_name = 'enrollments/my_courses.html'
    context_object_name = 'enrollments'

    def get_queryset(self):
        return Enrollment.objects.filter(student=self.request.user)

class CourseStudentsView(InstructorRequiredMixin, ListView):
    template_name = 'enrollments/course_students.html'
    context_object_name = 'enrollments'

    def get_course(self):
        return get_object_or_404(Course, pk=self.kwargs['course_pk'], instructor=self.request.user)

    def get_queryset(self):
        return Enrollment.objects.filter(course=self.get_course()).select_related('student')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.get_course()
        return context


class GradeUpdateView(InstructorRequiredMixin, UpdateView):
    form_class = GradeForm
    template_name = 'enrollments/grade_form.html'

    def get_queryset(self):
        # فقط ثبت‌نام‌های دوره‌های همین مدرس
        return Enrollment.objects.filter(course__instructor=self.request.user).select_related('student', 'course')

    def get_success_url(self):
        messages.success(self.request, 'نمره و ارزیابی ثبت شد.')
        return reverse('enrollments:students', kwargs={'course_pk': self.object.course_id}) # type: ignore