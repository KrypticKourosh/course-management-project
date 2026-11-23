from django import forms

from .models import Course, Session


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'category', 'capacity', 'start_date', 'end_date', 'price')
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned = super().clean()
        start, end = cleaned.get('start_date'), cleaned.get('end_date')
        if start and end and end < start:
            raise forms.ValidationError('تاریخ پایان نمی‌تواند قبل از شروع باشد.')
        return cleaned


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('title', 'date', 'start_time', 'end_time')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned = super().clean()
        start, end = cleaned.get('start_time'), cleaned.get('end_time')
        if start and end and end <= start:
            raise forms.ValidationError('ساعت پایان باید بعد از شروع باشد.')
        return cleaned