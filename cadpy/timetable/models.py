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

class WorkingDays(models.Model):
        nubdays = models.IntegerField(blank=True, null=True)
        days= models.CharField( max_length = 255,null = True,blank = True )
        starttime=models.CharField(max_length = 255,null = True,blank = True)
        endtime=models.CharField(max_length = 255,null = True,blank = True)
        slot= models.CharField( max_length = 255,null = True,blank = True )
