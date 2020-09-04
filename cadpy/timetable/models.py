from django.db import models

# Create your models here.
class Lecturer(models.Model):
    name = models.CharField(max_length=100,blank=True)
    center = models.CharField(max_length=100,blank=True)
    employee_id = models.CharField(max_length=6,blank=True)
    building=models.CharField(max_length=100,blank=True)
    faculty = models.CharField(max_length=100,blank=True)
    level = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=100,blank=True)
    rank=models.CharField(max_length=100,blank=True)
    objects = models.Manager()

class Subjects(models.Model):
    offeredYear=models.CharField(max_length=4,blank=True)
    offeredSemester=models.CharField(max_length=100,blank=True)
    subjectName=models.CharField(max_length=100,blank=True)
    subjectCode=models.CharField(max_length=10,blank=True)
    noLecHours=models.IntegerField(blank=True, null=True)
    noTutHours=models.IntegerField(blank=True, null=True)
    noLabHours=models.IntegerField(blank=True, null=True)
    noEveHours=models.IntegerField(blank=True, null=True)
    objects = models.Manager()