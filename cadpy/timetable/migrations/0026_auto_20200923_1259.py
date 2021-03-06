# Generated by Django 3.0.8 on 2020-09-23 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0025_merge_20200923_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnavailableRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
                ('start_time', models.CharField(max_length=10)),
                ('end_time', models.CharField(max_length=10)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Building')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Room')),
            ],
        ),
        migrations.AddConstraint(
            model_name='unavailableroom',
            constraint=models.UniqueConstraint(fields=('day', 'start_time', 'end_time', 'room', 'building'), name='unavailableroom_unique_row'),
        ),
    ]
