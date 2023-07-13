from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
from .forms import SubjectModelForm, UniversityGroupModelForm, StudentDetailForm


class SubjectCreate(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    form_class = SubjectModelForm
    template_name = 'core/subject/subject_create.html'

    def test_func(self):
        return self.request.user.has_perm('core.add_subject')


class SubjectUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    form_class = SubjectModelForm
    template_name = 'core/subject/subject_update.html'

    def test_func(self):
        return self.request.user.has_perm('core.change_subject')


class SubjectList(generic.ListView):
    model = Subject
    template_name = 'core/subject/subject_list.html'


class SubjectDetail(generic.DetailView):
    model = Subject
    template_name = 'core/subject/subject_detail.html'


class UniversityGroupCreate(generic.CreateView):
    model = UniversityGroup
    form_class = UniversityGroupModelForm
    template_name = 'core/uni_group/uni_group_create.html'
    success_url = 'students-add/'


class UniversityGroupAddStudent(generic.CreateView):
    model = StudentDetail
    form_class = StudentDetailForm
    template_name = 'core/uni_group/uni_group_create.html'


class StudentList(generic.ListView):
    queryset = User.objects.filter(groups__name='Student')
    paginate_by = 25
    template_name = 'core/subject/student_list.html'
