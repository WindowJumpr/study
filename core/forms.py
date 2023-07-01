from django.forms import ModelForm
from .models import *
from django.utils.translation import gettext_lazy as _


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        exclude = ('teacher',)
        labels = {
            "name": _("subject name")
        }
