from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

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


class WorkingDays(models.Model):
    nubdays = models.IntegerField(blank=True, null=True)
    days = models.CharField(max_length=255, null=True, blank=True)
    starttime = models.CharField(max_length=255, null=True, blank=True)
    endtime = models.CharField(max_length=255, null=True, blank=True)
    slot = models.CharField(max_length=255, null=True, blank=True)


class Tags(models.Model):
    label = models.CharField(max_length=25, unique=True)
    color = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.label


class AcademicYearSemester(models.Model):
    academic_year = models.IntegerField(default=1)
    academic_semester = models.IntegerField(default=1)

    class Meta:
        db_table = "timetable_academicyearsemester"
        constraints = [
            models.UniqueConstraint(
                fields=['academic_year', 'academic_semester'], name='academic_details')
        ]

    def __str__(self):
        return 'Y' + str(self.academic_year) + '.S' + str(self.academic_semester)


class Programme(models.Model):
    programme_name = models.CharField(max_length=100)
    programme_abbv = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.programme_abbv


class Group(models.Model):
    academic_year_semester = models.ForeignKey(
        AcademicYearSemester, on_delete=models.CASCADE)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    group_no = models.CharField(max_length=2)
    student_count = models.IntegerField(null=True, blank=True)
    generated_group = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['academic_year_semester', 'programme', 'group_no'], name='student_details')
        ]

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
    generated_subgroup = models.CharField(
        max_length=100, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['group', 'subgroup_no'], name='subgroup_details')
        ]

    def generate_subgroup_id(self):
        sub_group_id = self.group.generated_group + '.' + str(self.subgroup_no)
        return sub_group_id
    # str not defined


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


class Session(models.Model):
    lecturers = models.ManyToManyField(Lecturer)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    subgroup_id = models.ForeignKey(
        Subgroup, on_delete=models.CASCADE, null=True, blank=True)
    student_count = models.IntegerField(default=1)
    duration = models.IntegerField(default=1)
    consecutive_session = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    objects = models.Manager()

    def get_lecturers(self):
        if self.lecturers:
            return '%s' % " , ".join([lecturer.name for lecturer in self.lecturers.all()])


class ConsecutiveSession(models.Model):
    session1 = models.ForeignKey(
        Session, related_name='consecutivesession_session1', on_delete=models.CASCADE,)
    session2 = models.ForeignKey(
        Session, related_name='consecutivesession_session2', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['session1', 'session2'], name='consecutive_details')
        ]


class GroupBlockedTimeslots(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subgroup = models.ForeignKey(
        Subgroup, on_delete=models.CASCADE, null=True, blank=True)
    day = models.CharField(max_length=20)
    starttime = models.CharField(max_length=50)
    endtime = models.CharField(max_length=50)


class LecturerBlockedTimeslots(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    starttime = models.CharField(max_length=50)
    endtime = models.CharField(max_length=50)


class SessionBlockedTimeslots(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    starttime = models.CharField(max_length=50)
    endtime = models.CharField(max_length=50)


class ParallelSession(models.Model):
    sessions = models.ManyToManyField(Session)


class NonParallelSession(models.Model):
    sessions = models.ManyToManyField(Session)

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


class UnavailableRoom(models.Model):
    day = models.CharField(max_length=10)
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    objects = models.Manager()

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['day', 'start_time', 'end_time', 'room', 'building'], name='unavailableroom_unique_row'),
    #     ]


class LecturerRoom(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    objects = models.Manager()


class GroupRoom(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    objects = models.Manager()


class SubGroupRoom(models.Model):
    subgroup = models.ForeignKey(Subgroup, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    objects = models.Manager()


class TagRoom(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    objects = models.Manager()


class SubjectTagRoom(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    objects = models.Manager()


class SessionRoom(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    objects = models.Manager()


class ConsecutiveSessionRoom(models.Model):
    session1 = models.ForeignKey(
        Session, on_delete=models.CASCADE, related_name='session1')
    session2 = models.ForeignKey(
        Session, on_delete=models.CASCADE, related_name='session2')
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    objects = models.Manager()


#########################################################################


class MockWorkingDays(models.Model):
    nubdays = models.IntegerField(blank=True, null=True)
    days = models.CharField(max_length=255, null=True, blank=True)
    starttime = models.CharField(max_length=255, null=True, blank=True)
    endtime = models.CharField(max_length=255, null=True, blank=True)
    slot = models.CharField(max_length=255, null=True, blank=True)

    def get_all_days(self):
        return self.days.split(',')
