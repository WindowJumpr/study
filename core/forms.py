from django import forms
from django.contrib.auth.models import User

from .models import Subject, UniversityGroup, StudentDetail


class SubjectModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teacher'].queryset = User.objects.filter(groups__name='Teacher')

    class Meta:
        model = Subject
        fields = '__all__'


class UniversityGroupModelForm(forms.ModelForm):

    class Meta:
        model = UniversityGroup
        fields = ('name', )


class StudentDetailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].queryset = User.objects.filter(groups__isnull=True)

    class Meta:
        model = StudentDetail
        exclude = ('university_group', )
