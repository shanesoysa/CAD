# Generated by Django 3.1 on 2020-08-18 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_auto_20200814_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingDays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nubdays', models.IntegerField(blank=True, null=True)),
                ('days', models.CharField(blank=True, max_length=255, null=True)),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
                ('slot', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
