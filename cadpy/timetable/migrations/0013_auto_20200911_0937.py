# Generated by Django 3.1 on 2020-09-11 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0012_auto_20200911_0834'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='group',
            constraint=models.UniqueConstraint(fields=('academic_year_semester', 'programme', 'group_no'), name='student_details'),
        ),
    ]
