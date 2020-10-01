# Generated by Django 3.0.8 on 2020-09-29 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0029_lecturerroom_building'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubGroupRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable.Building')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Room')),
                ('subgroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Subgroup')),
            ],
        ),
        migrations.CreateModel(
            name='GroupRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable.Building')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Group')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Room')),
            ],
        ),
    ]
