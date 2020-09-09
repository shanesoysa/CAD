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


class AcademicYearSemester(models.Model):
    academic_year = models.IntegerField(default=1)
    academic_semester = models.IntegerField(default=1)

    def __str__(self):
        return 'Y' + str(self.academic_year) + '.S' + str(self.academic_semester)


class Programme(models.Model):
    programme_name = models.CharField(max_length=100)
    programme_abbv = models.CharField(max_length=20)

    def __str__(self):
        return self.programme_abbv


class Group(models.Model):
    academic_year_semester = models.ForeignKey(
        AcademicYearSemester, on_delete=models.CASCADE)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    group_no = models.CharField(max_length=2)
    student_count = models.IntegerField(null=True, blank=True)
    generated_group = models.CharField(max_length=100, blank=True, null=True)

    def generate_group_id(self):
        group_id = self.academic_year_semester.__str__() + '.' + self.programme.__str__()

        if int(self.group_no) < 10:
            group_id += '.0' + self.group_no
        else:
            group_id += '.' + self.group_no
        print(group_id)
        return group_id
    # str not defined


class Subgroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subgroup_no = models.IntegerField(default=1)
    generated_subgroup = models.CharField(max_length=100, blank=True)

    def generate_subgroup_id(self):
        sub_group_id = self.group.generated_group + '.' + str(self.subgroup_no)
        return sub_group_id
    # str not defined
