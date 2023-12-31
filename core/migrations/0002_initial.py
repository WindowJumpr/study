# Generated by Django 4.1.7 on 2023-06-29 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(auto_now_add=True)),
                ('study_form', models.CharField(choices=[('B', 'Budget day form'), ('P', 'Paid day form'), ('BR', 'Budget remote form'), ('PR', 'Paid remote form')], max_length=2)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('hours', models.IntegerField()),
                ('exam', models.BooleanField(default=None)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UniversityGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('students', models.ManyToManyField(through='core.StudentDetail', to=settings.AUTH_USER_MODEL)),
                ('subjects', models.ManyToManyField(to='core.subject')),
            ],
        ),
        migrations.AddField(
            model_name='studentdetail',
            name='university_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.universitygroup'),
        ),
        migrations.CreateModel(
            name='RecordSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(blank=True, null=True)),
                ('exam', models.BooleanField(default=False)),
                ('record_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.recordbook')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subject')),
            ],
        ),
        migrations.AddField(
            model_name='recordbook',
            name='subject',
            field=models.ManyToManyField(through='core.RecordSubject', to='core.subject'),
        ),
    ]
