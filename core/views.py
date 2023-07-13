from django.http import HttpResponseRedirect, Http404
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

    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponseRedirect(reverse('group-add-students', kwargs={'pk': self.object.id}))


class UniversityGroupAddStudent(generic.CreateView):
    model = StudentDetail
    form_class = StudentDetailForm
    template_name = 'core/uni_group/uni_group_add_students.html'
    success_url = '/'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__id = None
        self.uni_group = None

    def get(self, request, *args, **kwargs):
        self.__id = self.find_id(self.request.path)
        self.uni_group = UniversityGroup.objects.get(id=self.__id)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.__id = self.find_id(self.request.path)
        self.uni_group = UniversityGroup.objects.get(id=self.__id)
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.uni_group.id
        return context

    def form_valid(self, form):
        print(self.uni_group)
        form.instance.university_group = self.uni_group
        super().form_valid(form)
        group = Group.objects.get(name='Student')
        form.instance.student.groups.add(group)
        form.instance.save()
        return HttpResponseRedirect(self.request.path_info)

    @staticmethod
    def find_id(url):
        temp_url_list = url.split('/')
        for slug in temp_url_list:
            if slug.isalnum():
                return int(slug)
        raise Http404()


class UniversityGroupDetailView(generic.DetailView):
    model = UniversityGroup
    template_name = 'core/subject/subject_detail.html'


class StudentList(generic.ListView):
    queryset = User.objects.filter(groups__name='Student')
    paginate_by = 25
    template_name = 'core/subject/student_list.html'
