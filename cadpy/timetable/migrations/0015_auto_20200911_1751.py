# Generated by Django 3.1 on 2020-09-11 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0014_auto_20200911_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='color',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='tags',
            name='label',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
