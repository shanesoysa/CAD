# Generated by Django 3.0.8 on 2020-09-28 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0027_auto_20200928_0610'),
    ]

    operations = [
        migrations.CreateModel(
            name='LecturerRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Lecturer')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Room')),
            ],
        ),
    ]