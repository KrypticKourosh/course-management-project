from django import forms

from .models import Enrollment


class GradeForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ('grade', 'evaluation')

    def clean_grade(self):
        grade = self.cleaned_data.get('grade')
        if grade is not None and not (0 <= grade <= 20):
            raise forms.ValidationError('نمره باید بین ۰ تا ۲۰ باشد.')
        return grade