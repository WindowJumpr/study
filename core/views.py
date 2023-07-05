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


class SubjectList(generic.ListView):
    model = Subject


class SubjectDetail(generic.DetailView):
    model = Subject


class StudentList(generic.ListView):
    queryset = User.objects.filter(groups__name='Student')
    paginate_by = 25
    template_name = 'core/student_list.html'
