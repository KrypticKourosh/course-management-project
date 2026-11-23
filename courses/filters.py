import django_filters
from django import forms

from .models import Category, Course


class CourseFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'placeholder': 'جستجو بر اساس عنوان...'}),
    )
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        empty_label='همه موضوعات',
    )

    class Meta:
        model = Course
        fields = []