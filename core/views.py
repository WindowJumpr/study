from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import SubjectForm
from .models import *


class SubjectCreate(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    form_class = SubjectForm
    template_name = 'core/subject_create.html'

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.has_perm('core.add_subject')


class SubjectUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Subject
    form_class = SubjectForm

    def test_func(self):
        return self.request.user.has_perm('core.change_subject')


class SubjectList(generic.ListView):
    model = Subject


class SubjectDetail(generic.DetailView):
    model = Subject


class StudentList(generic.ListView):
    queryset = User.objects.filter(groups__name='Student')
    paginate_by = 25
    template_name = 'core/student_list.html'
