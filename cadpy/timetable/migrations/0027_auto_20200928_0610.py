# Generated by Django 3.0.8 on 2020-09-28 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0026_auto_20200923_1259'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='unavailableroom',
            name='unavailableroom_unique_row',
        ),
    ]