from django.urls import path
from .views import *


urlpatterns = [
    path('add-subject/', SubjectCreate.as_view(), name='add-subject'),
    path('subject-detail/<int:pk>/', SubjectDetail.as_view(), name='subject-detail'),
    path('subject-update/<int:pk>', SubjectUpdate.as_view(), name='subject-update'),
]
