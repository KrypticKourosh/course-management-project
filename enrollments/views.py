from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView

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