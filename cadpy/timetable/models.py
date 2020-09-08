from django.db import models

# Create your models here.


class Lecturer(models.Model):
    name = models.CharField(max_length=100, blank=True)
    center = models.CharField(max_length=100, blank=True)
    employee_id = models.CharField(max_length=6, blank=True)
    building = models.CharField(max_length=100, blank=True)
    faculty = models.CharField(max_length=100, blank=True)
    level = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=100, blank=True)
    rank = models.CharField(max_length=100, blank=True)
    objects = models.Manager()


class Subjects(models.Model):
    offeredYear = models.CharField(max_length=4, blank=True)
    offeredSemester = models.CharField(max_length=100, blank=True)
    subjectName = models.CharField(max_length=100, blank=True)
    subjectCode = models.CharField(max_length=10, blank=True)
    noLecHours = models.IntegerField(blank=True, null=True)
    noTutHours = models.IntegerField(blank=True, null=True)
    noLabHours = models.IntegerField(blank=True, null=True)
    noEveHours = models.IntegerField(blank=True, null=True)
    objects = models.Manager()

# ranul ##################################################################


class Building(models.Model):
    name = models.CharField(max_length=30, unique=True)
    objects = models.Manager()


class Room(models.Model):
    name = models.CharField(max_length=30)
    capacity = models.IntegerField()
    room_type = models.CharField(max_length=30)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    objects = models.Manager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'building'], name='unique_row'),
        ]

#########################################################################
