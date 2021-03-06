# Generated by Django 3.0.8 on 2020-08-18 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_auto_20200814_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('capacity', models.IntegerField()),
                ('room_type', models.CharField(max_length=30)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.Building')),
            ],
        ),
    ]
