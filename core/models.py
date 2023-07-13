from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import User, Group
from django.urls import reverse


class Subject(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    hours = models.IntegerField()
    exam = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}, teacher is {self.teacher.username}'

    def get_absolute_url(self):
        return reverse('subject-detail', kwargs={'pk': self.pk})


class Semester(models.Model):
    name = models.CharField(max_length=50)
    subjects = models.ManyToManyField(Subject)
    current = models.BooleanField()

    def __str__(self):
        return f'{self.name}'


class UniversityGroup(models.Model):
    name = models.CharField(max_length=50)
    students = models.ManyToManyField(User, through="StudentDetail")
    semesters = models.ManyToManyField(Semester)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('university-group-detail', kwargs={'pk': self.pk})


@receiver(post_save, sender=UniversityGroup)
def create_semesters(sender, instance, created, **kwargs):
    if created:
        semester_names = [f'{s} semester {instance.name}' for s in range(1, 5)]

        semesters = []
        for i, name in enumerate(semester_names):
            current = True if i == 0 else False
            semester = Semester(name=name, current=current)
            semesters.append(semester)

        Semester.objects.bulk_create(semesters)

        instance.semesters.add(*semesters)
        instance.save()


class StudentDetail(models.Model):
    FORM_OF_STUDY_CHOICES = (
        ('B', 'Budget day form'),
        ('P', 'Paid day form'),
        ('BR', 'Budget remote form'),
        ('PR', 'Paid remote form'),
    )
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    university_group = models.ForeignKey(UniversityGroup, on_delete=models.CASCADE)
    entry_date = models.DateField(auto_now_add=True)
    study_form = models.CharField(max_length=2, choices=FORM_OF_STUDY_CHOICES)


class RecordBook(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ManyToManyField(Subject, through='RecordSubject')

    def __str__(self):
        return f"{self.student.username}'s record book"


class RecordSubject(models.Model):
    record_book = models.ForeignKey(RecordBook, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.IntegerField()
    mark = models.IntegerField(null=True)
    exam = models.BooleanField(default=False)

