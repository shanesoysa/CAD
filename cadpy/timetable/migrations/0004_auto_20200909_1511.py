# Generated by Django 3.1 on 2020-09-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_auto_20200819_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subgroup',
            name='generated_subgroup',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]