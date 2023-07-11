from django import forms
from django.contrib.auth.models import User
from .models import Subject


class SubjectModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teacher'].queryset = User.objects.filter(groups__name='Teacher')

    class Meta:
        model = Subject
        fields = '__all__'
