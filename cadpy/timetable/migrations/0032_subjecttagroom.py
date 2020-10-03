# Generated by Django 3.0.8 on 2020-09-29 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0031_tagroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectTagRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable.Building')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Room')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Subjects')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Tags')),
            ],
        ),
    ]
