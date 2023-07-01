from django.views import generic
from .forms import SubjectForm
from .models import *


class SubjectCreate(generic.CreateView):
    form_class = SubjectForm
    template_name = 'core/subject_create.html'

    def form_valid(self, form):
        form.instance.teacher = User.objects.filter(groups__name='Teacher').first()
        return super().form_valid(form)


class SubjectUpdate(generic.UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'core/subject_update.html'


class SubjectDetail(generic.DetailView):
    model = Subject
    template_name = 'core/subject_detail.html'
