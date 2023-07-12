# Generated by Django 4.1.7 on 2023-07-12 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_recordsubject_semester_alter_recordsubject_mark_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='universitygroup',
            name='subjects',
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('current', models.BooleanField()),
                ('subjects', models.ManyToManyField(to='core.subject')),
            ],
        ),
        migrations.AddField(
            model_name='universitygroup',
            name='semesters',
            field=models.ManyToManyField(blank=True, null=True, to='core.semester'),
        ),
    ]
