from django.urls import path
from .views import *


urlpatterns = [
    path('subject-create/', SubjectCreate.as_view(), name='add-subject'),
    path('subject-update/<int:pk>', SubjectUpdate.as_view(), name='subject-update'),
    path('subject-detail/<int:pk>/', SubjectDetail.as_view(), name='subject-detail'),
    path('subject-list/', SubjectList.as_view(), name='subject-list'),
    path('student-list/', StudentList.as_view(), name='student-list'),
    path('universitygroup-create/', UniversityGroupCreate.as_view(), name='uni_group-create'),
    path('universitygroup-create/<int:pk>/students-add/', UniversityGroupAddStudent.as_view(),
         name='group-add-students'),
    path('universitygroup-detail/<int:pk>/', UniversityGroupDetailView.as_view(), name='uni_group-detail'),
]
