from django.db.models import fields
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.context_processors import request
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import ListView
from django.views.generic import View
from django.views import generic
from django.http import JsonResponse
from .models import GroupRoom, LecturerRoom, SessionRoom, SubGroupRoom, Subgroup, Group, Programme, AcademicYearSemester, SubjectTagRoom, TagRoom, Tags, UnavailableRoom
from .models import Subgroup, Group, Programme, AcademicYearSemester, Tags
from django.db.utils import IntegrityError
# import sys
from .models import Lecturer as Lecturer1
from .models import WorkingDays
from .models import Subjects as Subjects1
from .models import Session as Session1
from .models import ParallelSession

from django.views.generic import DetailView
from .models import Building as BuildingModel, Room as RoomModel
from django.core import serializers

from .models import Session, ParallelSession, NonParallelSession, ConsecutiveSession
from .models import NonParallelSession, ConsecutiveSession
from .models import GroupBlockedTimeslots, LecturerBlockedTimeslots, SessionBlockedTimeslots
from django.core import serializers
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
# Create your views here.


def index(request):
    return render(request, 'home.html')


def Validations(request):
    employee_id1 = request.GET.get('employee_id1', None)
    data = {
        'is_taken': Lecturer1.objects.filter(employee_id__iexact=employee_id1).exists()
    }

    return JsonResponse(data)


class Lecturer(ListView):
    model = Lecturer1
    template_name = 'list_lecturers.html'
    context_object_name = 'lecturers'


class AddLecturer(View):
    def get(self, request):

        try:
            name1 = request.GET.get('name', None)
            center1 = request.GET.get('center', None)
            employee_id1 = request.GET.get('employee_id', None)
            building1 = request.GET.get('building', None)
            faculty1 = request.GET.get('faculty', None)
            level1 = request.GET.get('level', None)
            department1 = request.GET.get('department', None)
            rank1 = request.GET.get('rank', None)

            obj = Lecturer1.objects.create(
                name=name1,
                center=center1,
                employee_id=employee_id1,
                building=building1,
                faculty=faculty1,
                level=level1,
                department=department1,
                rank=rank1
            )

            lecturer = {'id': obj.id, 'name': obj.name, 'center': obj.center, 'employee_id': obj.employee_id,
                        'building': obj.building, 'faculty': obj.faculty, 'level': obj.level, 'department': obj.department, 'rank': obj.rank}

            data = {
                'lecturer': lecturer
            }
            print("successfull")

            return JsonResponse(data)

        except:

            print("fail adding data")
            pass


class UpdateLecturer(View):
    try:
        def get(self, request):
            id1 = request.GET.get('id', None)
            name1 = request.GET.get('name', None)
            center1 = request.GET.get('center', None)
            employee_id1 = request.GET.get('employee_id', None)
            building1 = request.GET.get('building', None)
            faculty1 = request.GET.get('faculty', None)
            level1 = request.GET.get('level', None)
            department1 = request.GET.get('department', None)
            rank1 = request.GET.get('rank', None)

            obj = Lecturer1.objects.get(id=id1)
            obj.name = name1
            obj.center = center1
            obj.employee_id = employee_id1
            obj.building = building1
            obj.faculty = faculty1
            obj.level = level1
            obj.department = department1
            obj.rank = rank1

            obj.save()

            lecturer = {'id': obj.id, 'name': obj.name, 'center': obj.center, 'employee_id': obj.employee_id,
                        'building': obj.building, 'faculty': obj.faculty, 'level': obj.level, 'department': obj.department, 'rank': obj.rank}

            data = {
                'lecturer': lecturer
            }
            return JsonResponse(data)

    except:

        print("lecturer update failed")
        pass


class DeleteLecturer(View):
    try:
        def get(self, request):
            id1 = request.GET.get('id', None)
            Lecturer1.objects.get(id=id1).delete()
            data = {
                'deleted': True
            }
            return JsonResponse(data)
    except:

        print("lecturer delete failed")
        pass


def side(request):
    return render(request, 'side.html')


class Workingdays(ListView):
    model = WorkingDays
    template_name = 'addDays.html'
    context_object_name = 'days'
    # print(model)


class Adddays(View):
    def get(self, request):

        try:
            ndays = request.GET.get('numdays', None)
            workingdays = request.GET.get('workingdays', None)
            stime = request.GET.get('stime', None)
            etime = request.GET.get('etime', None)
            slots = request.GET.get('slots', None)

          #  x = workingdays.split(',')
           # print(x)

          #  for y in x:
            # print(y)
            # print("successfull")
            obj = WorkingDays.objects.create(
                nubdays=ndays,
                days=workingdays,
                starttime=stime,
                endtime=etime,
                slot=slots,
            )

            day = {'id': obj.id, 'nubdays': obj.nubdays, 'days': obj.days,
                   'starttime': obj.starttime, 'endtime': obj.endtime, 'slot': obj.slot}
            data = {
                'day': day
            }
            # print("successfull")
            # print(data)
            return JsonResponse(data)

        except:

            print("fail adding data")
            pass


class Updatedays(View):
    def get(self, request):

        try:
            id1 = request.GET.get('id', None)
            ndays = request.GET.get('numdays', None)
            workingdays = request.GET.get('workingdays', None)
            stime = request.GET.get('stime', None)
            etime = request.GET.get('etime', None)
            slots = request.GET.get('slots', None)

            obj = WorkingDays.objects.get(id=id1)
            obj.nubdays = ndays
            obj.days = workingdays
            obj.starttime = stime
            obj.endtime = etime
            obj.slot = slots
            obj.save()

            day = {'id': obj.id, 'nubdays': obj.nubdays, 'days': obj.days,
                   'starttime': obj.starttime, 'endtime': obj.endtime, 'slot': obj.slot}

            data = {
                'day': day
            }
            return JsonResponse(data)

        except:

            print("days update failed")
            pass


def home(request):
    return render(request, 'home.html')


class Deletedays(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        WorkingDays.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


def timetables(request):
    return render(request, 'timetables.html')


class Subjects(ListView):
    model = Subjects1
    template_name = 'list_subjects.html'
    context_object_name = 'subjects'


class AddSubjects(View):
    def get(self, request):

        try:
            offeredYear1 = request.GET.get('offeredYear', None)
            offeredSemester1 = request.GET.get('offeredSemester', None)
            subjectName1 = request.GET.get('subjectName', None)
            subjectCode1 = request.GET.get('subjectCode', None)
            noLecHours1 = request.GET.get('noLecHours', None)
            noTutHours1 = request.GET.get('noTutHours', None)
            noLabHours1 = request.GET.get('noLabHours', None)
            noEveHours1 = request.GET.get('noEveHours', None)

            obj = Subjects1.objects.create(
                offeredYear=offeredYear1,
                offeredSemester=offeredSemester1,
                subjectName=subjectName1,
                subjectCode=subjectCode1,
                noLecHours=noLecHours1,
                noTutHours=noTutHours1,
                noLabHours=noLabHours1,
                noEveHours=noEveHours1
            )

            subject = {'id': obj.id, 'offeredYear': obj.offeredYear, 'offeredSemester': obj.offeredSemester, 'subjectName': obj.subjectName,
                       'subjectCode': obj.subjectCode, 'noLecHours': obj.noLecHours, 'noTutHours': obj.noTutHours, 'noLabHours': obj.noLabHours, 'noEveHours': obj.noEveHours}

            data = {
                'subject': subject
            }
            print("successfull")

            return JsonResponse(data)

        except:
            print("fail adding data")
            pass


class UpdateSubject(View):
    try:
        def get(self, request):
            id1 = request.GET.get('id', None)
            offeredYear1 = request.GET.get('offeredYear', None)
            offeredSemester1 = request.GET.get('offeredSemester', None)
            subjectName1 = request.GET.get('subjectName', None)
            subjectCode1 = request.GET.get('subjectCode', None)
            noLecHours1 = request.GET.get('noLecHours', None)
            noTutHours1 = request.GET.get('noTutHours', None)
            noLabHours1 = request.GET.get('noLabHours', None)
            noEveHours1 = request.GET.get('noEveHours', None)

            obj = Subjects1.objects.get(id=id1)
            obj.offeredYear = offeredYear1
            obj.offeredSemester = offeredSemester1
            obj.subjectName = subjectName1
            obj.subjectCode = subjectCode1
            obj.noLecHours = noLecHours1
            obj.noTutHours = noTutHours1
            obj.noLabHours = noLabHours1
            obj.noEveHours = noEveHours1

            obj.save()

            subject = {'id': obj.id, 'offeredYear': obj.offeredYear, 'offeredSemester': obj.offeredSemester, 'subjectName': obj.subjectName,
                       'subjectCode': obj.subjectCode, 'noLecHours': obj.noLecHours, 'noTutHours': obj.noTutHours, 'noLabHours': obj.noLabHours, 'noEveHours': obj.noEveHours}

            data = {
                'subject': subject
            }
            return JsonResponse(data)

    except:

        print("subject update failed")
        pass


class DeleteSubject(View):
    try:
        def get(self, request):
            id1 = request.GET.get('id', None)
            Subjects1.objects.get(id=id1).delete()
            data = {
                'deleted': True
            }
            return JsonResponse(data)
    except:

        print("lecturer delete failed")
        pass


class Session(generic.ListView):
    model = Session1
    template_name = 'session_allocate.html'
    context_object_name = 'sessions'
    queryset = Session1.objects.prefetch_related('lecturers')

    def get_context_data(self, **kwargs):
        context = super(Session, self).get_context_data(**kwargs)
        context.update({
            'lecturers': Lecturer1.objects.all(),
            'tags': Tags.objects.all(),
            'subjects': Subjects1.objects.all(),
            'groups': Group.objects.all(),
            'subgroups': Subgroup.objects.select_related('group'),
            'sessions': Session1.objects.prefetch_related('group_id', 'subject', 'tag', 'subgroup_id').all(),
            # 'more_context': Model.objects.all(),
        })
        return context

    # def get_queryset(self):
    #     return Session1.objects.order_by('id')


# class DeleteSession(View):
#     try:
#         def get(self, request):
#             id1 = request.GET.get('id', None)
#             obj = Session1.objects.get(id=id1).delete()

#             # obj.lecturers.remove(id=id1)

#             data = {
#                 'deleted': True
#             }
#             return JsonResponse(data)
#     except:
#         print("session delete failed")
#         pass


class AddSession(View):
    def get(self, request):

        try:
            lecturers = request.GET.getlist('lecturers[]')
            subjects = request.GET.get('subjects', None)
            tags = request.GET.get('tags', None)
            students = request.GET.get('students', None)
            groups = request.GET.get('groups', None)
            duration = request.GET.get('duration', None)

            obj = Session1.objects.create(
                subject_id=subjects,
                tag_id=tags,
                student_count=students,
                group_id_id=groups,
                duration=duration
            )

            latestid = Session1.objects.latest('id')
            # for lec in lecturers:
            #     print(lec)
            #     obj.lecturers.add(lec)

            for i in range(len(lecturers)):
                objlec = Lecturer1.objects.get(pk=lecturers[i])

                obj.lecturers.add(objlec)
                print(lecturers[i])
                # obj.lecturers.create(session_id=latestid,
                #                      lecturer_id=lecturers[i])

            result = {
                'success': lecturers
            }
            # print('lectureeeeeeeeeeeees:'+lecturers)
            return JsonResponse(result)

        except:
            print("fail adding data")
            pass
            # result = {
            #     'success': 'false'
            # }
            # return JsonResponse(result)


# Rehani's
class TagsView(generic.ListView):
    model = Tags
    template_name = 'tags/tags.html'


class DDView(generic.ListView):
    model = Tags
    template_name = 'students/st.html'


class DeleteTags(View):
    try:
        def get(self, request):
            id1 = request.GET.get('id', None)
            Tags.objects.get(id=id1).delete()
            data = {
                'deleted': True
            }
            return JsonResponse(data)
    except:
        print("tag delete failed")
        pass


class AddTagsView(View):
    def get(self, request):
        try:
            pname = request.GET.get('label', None)
            pabbv = request.GET.get('color', None)
            obj = Tags.objects.create(
                label=pname,
                color=pabbv
            )
            tags = {'id': obj.id, 'label': obj.label, 'color': obj.color}
            data = {
                'success_stat': 1,
                'student_tags': tags
            }
            return JsonResponse(data)
        except IntegrityError as e:
            data = {
                'success_stat': 0,
                'error_msg': 'Tag label or color already exists'
            }
            return JsonResponse(data)
        except Exception as ex:
            print("fail adding data")
            pass


class UpdateTags(View):
    def get(self, request):
        try:
            id1 = request.GET.get('id', None)
            pname = request.GET.get('label', None)
            pabbv = request.GET.get('color', None)

            obj = Tags.objects.get(id=id1)
            obj.label = pname
            obj.color = pabbv
            obj.save()
            tags = {'id': obj.id, 'label': obj.label, 'color': obj.color}
            data = {
                'success_stat': 1,
                'tags': tags
            }
            return JsonResponse(data)
        except IntegrityError as e:
            data = {
                'success_stat': 0,
                'error_msg': 'Tag label or color already exists'
            }
            return JsonResponse(data)
        except Exception as ex:
            print("tags update failed")
            data = {
                'success_stat': 0,
                'error_msg': 'Something went wrong'
            }
            return JsonResponse(data)


class StudentsView(generic.ListView):
    context_object_name = 'group_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Group.objects.exclude(generated_group=None)
    template_name = 'students/students.html'


class StudentsGenerationView(generic.ListView):
    context_object_name = 'group_list'

    def get_queryset(self):
        """Return the last five published questions."""
        listOfGroups = Group.objects.filter(generated_group=None)
        for group in listOfGroups:
            print(group.pk)
            # group_obj = Group.objects.get(pk=group.pk)
            group_id = group.generate_group_id()
            group.generated_group = group_id
            group.save()
        return Group.objects.exclude(generated_group=None)

    template_name = 'students/students.html'


class StudentsSubGroupGenerationView(generic.ListView):
    context_object_name = 'group_list'

    def get_queryset(self):
        """Return the last five published questions."""
        groupy = Group.objects.get(id=self.kwargs['pk'])
        for subgroup in groupy.subgroup_set.all():
            # group_obj = Group.objects.get(pk=group.pk)
            subgroup_id = subgroup.generate_subgroup_id()
            subgroup.generated_subgroup = subgroup_id
            subgroup.save()
        return Group.objects.exclude(generated_group=None)

    template_name = 'students/students.html'


class ProgrammesView(generic.ListView):
    model = Programme
    template_name = 'students/programmes.html'


class AddProgramme(View):
    def get(self, request):
        try:
            pname = request.GET.get('programme_name', None)
            pabbv = request.GET.get('programme_abbv', None)
            print(pname)
            print(pabbv)
            obj = Programme.objects.create(
                programme_name=pname,
                programme_abbv=pabbv
            )
            programme = {'id': obj.id, 'programme_name': obj.programme_name,
                         'programme_abbv': obj.programme_abbv}
            data = {
                'success_stat': 1,
                'programme': programme
            }
            return JsonResponse(data)
        except:
            data = {
                'success': 0,
                'error': 'Cannot save duplicate programme abbreviation'
            }
            print("fail adding data")
            return JsonResponse(data)


class DeleteProgramme(View):
    try:
        def get(self, request):
            id1 = request.GET.get('id', None)

            Programme.objects.get(id=id1).delete()

            data = {
                'deleted': True
            }
            return JsonResponse(data)
    except:
        print("programme delete failed")
        pass


class UpdateProgramme(View):
    def get(self, request):
        try:
            id1 = request.GET.get('id', None)
            pname = request.GET.get('programme_name', None)
            pabbv = request.GET.get('programme_abbv', None)

            obj = Programme.objects.get(id=id1)
            obj.programme_name = pname
            obj.programme_abbv = pabbv
            obj.save()
            programme = {'id': obj.id, 'programme_name': obj.programme_name,
                         'programme_abbv': obj.programme_abbv}
            data = {
                'success_stat': 1,
                'programme': programme
            }
            return JsonResponse(data)
        except:
            data = {
                'success_stat': 0,
                'error_msg': 'Cannot save duplicate programme abbreviation'
            }
            return JsonResponse(data)


class AcademicYearSemesterView(generic.ListView):
    model = AcademicYearSemester
    template_name = 'students/academic-year-semester.html'


class AddAcademicYearSemesterView(View):
    def get(self, request):

        try:
            ayear = request.GET.get('academic_year', None)
            asemester = request.GET.get('academic_semester', None)
            obj = AcademicYearSemester.objects.create(
                academic_year=ayear,
                academic_semester=asemester
            )

            academicyearsemester = {
                'id': obj.id, 'academic_year': obj.academic_year, 'academic_semester': obj.academic_semester}
            data = {
                'success_stat': 1,
                'academicyearsemester': academicyearsemester
            }
            print("successfull")
            return JsonResponse(data)
        except:
            data = {
                'success_stat': 0,
                'error_msg': 'Cannot save duplicate academic year and semester'
            }
            return JsonResponse(data)


class DeleteAcademicYearSemesterView(View):
    try:
        def get(self, request):
            id1 = request.GET.get('id', None)

            AcademicYearSemester.objects.get(pk=id1).delete()
            data = {
                'deleted': True
            }
            return JsonResponse(data)
    except:
        print("academic year-semester delete failed")
        pass


class UpdateAcademicYearSemesterView(View):
    def get(self, request):
        try:
            id1 = request.GET.get('id', None)
            ayear = request.GET.get('academic_year', None)
            asemester = request.GET.get('academic_semester', None)

            obj = AcademicYearSemester.objects.get(id=id1)
            obj.academic_year = ayear
            obj.academic_semester = asemester
            obj.save()
            academicyearsemester = {
                'id': obj.id, 'academic_year': obj.academic_year, 'academic_semester': obj.academic_semester}
            data = {
                'success_stat': 1,
                'academicyearsemester': academicyearsemester
            }
            return JsonResponse(data)
        except:
            print("Academic year-semester update failed")
            data = {
                'success_stat': 0,
                'error_msg': 'Cannot save duplicate academic year and semester'
            }
            return JsonResponse(data)


class GroupsView(generic.ListView):
    context_object_name = 'group_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['programme_ll'] = Programme.objects.all()
        context['academic_ll'] = AcademicYearSemester.objects.all()
        return context

    def get_queryset(self):
        """Return the last five published questions."""
        return Group.objects.filter(generated_group=None)
    template_name = 'students/generate-groups.html'


class AddStudentsView(View):
    def get(self, request):
        try:
            semester = request.GET.get('academic_year_semester', None)
            prog = request.GET.get('programme', None)
            count = request.GET.get('student_count', None)
            group_num = request.GET.get('group_no', None)

            yearSemester = AcademicYearSemester.objects.get(pk=semester)
            programm = Programme.objects.get(pk=prog)
            obj = Group.objects.create(
                academic_year_semester=yearSemester,
                programme=programm,
                group_no=group_num,
                student_count=count
            )
            student = {'id': obj.id, 'group_no': obj.group_no, 'student_count': obj.student_count, 'academic_year': obj.academic_year_semester.academic_year,
                       'academic_semester': obj.academic_year_semester.academic_semester, 'programme': obj.programme.programme_abbv}
            data = {
                'success_stat': 1,
                'student': student
            }
            return JsonResponse(data)
        except:
            data = {
                'success_stat': 0,
                'error_msg': 'Cannot save duplicate student group'
            }
            return JsonResponse(data)


class UpdateGroupsView(View):
    def get(self, request):
        try:
            id1 = request.GET.get('id', None)
            academics = request.GET.get('academic_year_semester', None)
            gprogramme = request.GET.get('programme', None)
            ggroup = request.GET.get('group_no', None)
            scount = request.GET.get('student_count', None)

            obj = Group.objects.get(id=id1)
            yearSemester = AcademicYearSemester.objects.get(pk=academics)
            programm = Programme.objects.get(pk=gprogramme)

            obj.academic_year_semester = yearSemester
            obj.programme = programm
            obj.group_no = ggroup
            obj.student_count = scount
            obj.save()
            group = {'id': obj.id, 'group_no': obj.group_no, 'student_count': obj.student_count, 'academic_year': obj.academic_year_semester.academic_year,
                     'academic_semester': obj.academic_year_semester.academic_semester, 'programme': obj.programme.programme_abbv}
            data = {
                'success_stat': 1,
                'group': group
            }
            return JsonResponse(data)
        except Exception as e:
            print(e)
            print("update of group failed")
            data = {
                'success_stat': 0,
                'error_msg': 'Cannot save duplicate student group'
            }
            return JsonResponse(data)


class DeleteStudentsView(View):
    try:
        def get(self, request):
            id1 = request.GET.get('id', None)

            Group.objects.get(id=id1).delete()
            data = {
                'deleted': True
            }
            return JsonResponse(data)
    except:
        print("Students delete failed")
        pass


class SubGroupsView(generic.DetailView):
    model = Group
    template_name = 'students/generate-subgroups.html'


class AddSubGroups(View):
    def get(self, request, pk):
        try:
            gp = request.GET.get('group', None)
            subgp = request.GET.get('subgroup_no', None)
            print(gp)
            print(subgp)
            groupObj = Group.objects.get(pk=pk)
            print(groupObj)
            obj = Subgroup.objects.create(
                group=groupObj,
                subgroup_no=subgp,
            )
            print('created')
            subgroup = {'id': obj.id, 'group': obj.group.generated_group,
                        'group_id': obj.group.id, 'subgroup_no': obj.subgroup_no}
            data = {
                'success_stat': 1,
                'subgroup': subgroup
            }
            print("successfull")
            return JsonResponse(data)
        except IntegrityError as e:
            # print("Oops!", sys.exc_info()[0], "occurred.")
            data = {
                'success_stat': 0,
                'error_msg': 'Cannot save duplicate subgroup'
            }
            print("fail adding data")
            return JsonResponse(data)
        except Exception as ex:
            print('Error: ', ex)
            pass


class DeleteSubGroups(View):
    def get(self, request, pk):
        try:
            id1 = request.GET.get('id', None)
            Subgroup.objects.get(id=id1).delete()
            data = {
                'deleted': True
            }
            return JsonResponse(data)
        except:
            print("programme delete failed")
            data = {
                'deleted': False
            }
            return JsonResponse(data)


class UpdateSubGroupsView(View):
    def get(self, request, pk):
        try:
            id1 = request.GET.get('id', None)
            pabbv = request.GET.get('subgroup_no', None)

            obj = Subgroup.objects.get(id=id1)
            obj.subgroup_no = pabbv
            obj.save()
            subgroup = {'id': obj.id, 'subgroup_no': obj.subgroup_no}
            data = {
                'success_stat': 1,
                'subgroup': subgroup
            }
            return JsonResponse(data)
        except IntegrityError as e:
            print("subgroup update failed")
            data = {
                'success_stat': 0,
                'error_msg': 'Cannot save duplicate subgroup'
            }
            return JsonResponse(data)
        except Exception as ex:
            print('Error: ', ex)
            pass


class AssignSessionsView(generic.ListView):
    model = Session1

    context_object_name = 'session_list'
    template_name = 'sessions/assign-sessions.html'

    def get_queryset(self):
        """Return all session objects"""
        return Session1.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags_list'] = Tags.objects.all()
        context['subject_list'] = Subjects1.objects.all()
        context['lecturer_list'] = Lecturer1.objects.all()
        context['work_days'] = WorkingDays.objects.all()
        context['group_list'] = Group.objects.exclude(generated_group=None)
        return context


class ConsecutiveSessionsView(generic.ListView):
    model = Session1
    template_name = 'sessions/consecutive-sessions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['session1'] = Session1.objects.get(pk=self.kwargs['pk'])
        context['subject_list'] = Subjects1.objects.all()
        context['tags_list'] = Tags.objects.all()
        context['group_list'] = Group.objects.exclude(generated_group=None)
        context['subgroup_list'] = Subgroup.objects.exclude(
            generated_subgroup=None)
        return context


class BlockTimeSlotsView(generic.ListView):
    model = Session1

    context_object_name = 'lecturer_list'
    template_name = 'sessions/blocked-timeslots.html'

    def get_queryset(self):
        """Return the lecturer objects with only specified fields"""
        return Lecturer1.objects.values('id', 'employee_id', 'name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['work_days'] = WorkingDays.objects.all()
        return context


class ParallelSessionsView(generic.ListView):
    model = ParallelSession
    template_name = 'sessions/parallel-sessions.html'


class NonParallelSessionsView(generic.ListView):
    model = NonParallelSession
    template_name = 'sessions/non-parallel-sessions.html'


@csrf_exempt
def create_consecutive_session(request, pk):
    try:
        list_json = request.POST.get('session2_id_list', None)
        session2_list = json.loads(session2_list)
        session1_obj = Session.objects.get(pk=pk)

        for session2 in session2_list:
            session2_obj = Session.objects.get(pk=session2)
            ConsecutiveSession.objects.create(
                session1=session1_obj,
                session2=session2_obj
            )

        data = {
            'success_stat': 1
        }
        return JsonResponse(data)
    except IntegrityError as e:
        data = {
            'error_msg': 'Consecutive Session already exists',
            'success_stat': 0
        }
        return JsonResponse(data)
    except Exception as ex:
        data = {
            'error_msg': 'unexpected error',
            'success_stat': 0
        }
        return JsonResponse(data)

@csrf_exempt
def create_consecutive_session(request, pk):
    try:
        list_json = request.POST.get('session2_id_list', None)
        session2_list = json.loads(list_json)
        session1_obj = Session1.objects.get(pk=pk)

        for session2 in session2_list:
            session2_obj = Session1.objects.get(pk=session2)
            ConsecutiveSession.objects.create(
                session1=session1_obj,
                session2=session2_obj
            )

        data = {
            'success_stat': 1
        }
        return JsonResponse(data)
    except IntegrityError as e:
        data = {
            'error_msg': 'Consecutive Session already exists',
            'success_stat': 0
        }
        return JsonResponse(data)
    except Exception as ex:
        print(ex)
        data = {
            'error_msg': 'unexpected error',
            'success_stat': 0
        }
        return JsonResponse(data)


def get_group_data(request, pk):
    group = request.GET.get('group', None)

    if(group == 'true'):
        group_list = Group.objects.exclude(
            generated_group=None).values('id', 'generated_group')
        group_type = 'group'
    else:
        group_list = Subgroup.objects.exclude(
            generated_subgroup=None).values('id', 'generated_subgroup')
        group_type = 'subgroup'
    data = {
        'groups': list(group_list),
        'group_type': group_type
    }
    return JsonResponse(data)


def get_group_data_2(request):
    group = request.GET.get('group_type', None)

    if(group == 'G'):
        group_list = Group.objects.exclude(
            generated_group=None).values('id', 'generated_group')
        group_type = 'group'
    elif(group == 'S'):
        group_list = Subgroup.objects.exclude(
            generated_subgroup=None).values('id', 'generated_subgroup')
        group_type = 'subgroup'
    else:
        group_list = Lecturer1.objects.values('id', 'employee_id', 'name')
        group_type = 'lecturer'
    data = {
        'groups': list(group_list),
        'group_type': group_type
    }
    return JsonResponse(data)

# get searched consecutive session


def get_consecutive_session(request, pk):
    try:
        batch = request.GET.get('batch', None)
        group = request.GET.get('group', None)
        subject = request.GET.get('subject', None)
        tag = request.GET.get('tag', None)

        if(batch == 'group'):
            session1 = Session1.objects.filter(subgroup_id=None).get(
                tag=tag, subject=subject, group_id=group)
        else:
            session1 = Session1.objects.get(
                tag=tag, subject=subject, subgroup_id=group)

        data = {
            'success_stat': 1,
            'id': session1.id,
            'subject_name': session1.subject.subjectName,
            'subject_code': session1.subject.subjectCode,
            'tag_label': session1.tag.label,
            'tag_color': session1.tag.color,
            'student_count': session1.student_count,
            'duration': session1.duration
        }
        if(batch == 'group'):
            data['group'] = session1.group_id.generated_group
        else:
            data['group'] = session1.subgroup_id.generated_subgroup

        return JsonResponse(data)
    except ObjectDoesNotExist as e:
        data = {
            'success_stat': 0,
            'error_msg': 'Session Not Found'
        }
        return JsonResponse(data)
    except MultipleObjectsReturned as ex:
        data = {
            'success_stat': 0,
            'error_msg': 'Multiple Sessions exists for search criteria'
        }
        return JsonResponse(data)


@csrf_exempt
def get_searched_session(request):
    try:
        lecturer = request.POST.get('lecturer', None)
        group = request.POST.get('group', None)
        subject = request.POST.get('subject', None)
        tag = request.POST.get('tag', None)
        conditions_list = {}

        # conditions to check if null
        if (group):
            conditions_list['group_id_id'] = group

        if (tag):
            conditions_list['tag_id'] = tag

        if (subject):
            conditions_list['subject_id'] = subject

        if (lecturer):
            conditions_list['lecturers'] = lecturer

        sessions = Session1.objects.filter(**conditions_list)
        sessions_list = []

        for session in sessions:
            sessions_list.append({'id': session.id,
                                  'group': session.group_id.generated_group,
                                  'subgroup': session.subgroup_id.generated_subgroup if session.subgroup_id != None else None,
                                  'subject_name': session.subject.subjectName,
                                  'subject_code': session.subject.subjectCode,
                                  'tag_label': session.tag.label,
                                  'tag_color': session.tag.color,
                                  'student_count': session.student_count,
                                  'duration': session.duration
                                  })
        # print(serializers.serialize('json', sessions_list)) Used only for classes
        data = {
            'success_stat': 1,
            'sessions_list': sessions_list
        }
        return JsonResponse(data)
    except Exception as e:
        data = {
            'success_stat': 0,
            'error_msg': 'Unexpected Error'
        }
        return JsonResponse(data)


@csrf_exempt
def createParallelSession(request):
    try:
        parallel = request.POST.get('parallel', None)
        session_list = request.POST.get('parallel_session_list', None)

        parallel_py = json.loads(parallel)
        session_list_py = json.loads(session_list)

        sobj = ParallelSession() if parallel_py == True else NonParallelSession()
        sobj.save()

        for index, session in enumerate(session_list_py):
            psession = Session1.objects.get(pk=session)
            sobj.sessions.add(psession)

        data = {
            'success_stat': 1,
            'parallel': parallel,
        }
        return JsonResponse(data)
    except Exception as e:
        data = {
            'success_stat': 0,
            'error_msg': 'Unexpected Error'
        }
        return JsonResponse(data)


@csrf_exempt
def create_blocked_session(request):
    try:
        days = request.POST.get('days_list', None)
        block = request.POST.get('block', None)
        block_id = request.POST.get('block_id', None)
        start_time = request.POST.get('start_time', None)
        end_time = request.POST.get('end_time', None)
        days_py = json.loads(days)

        obj = {}
        return_list = []
        if(block == 'L'):
            obj = Lecturer1.objects.get(pk=block_id)
            for d in days_py:
                l = LecturerBlockedTimeslots.objects.create(
                    lecturer=obj,
                    day=d,
                    starttime=start_time,
                    endtime=end_time
                )
                lecturer_info = {'id': l.lecturer.employee_id, 'name': l.lecturer.name,
                                 'day': l.day, 'start_time': l.starttime, 'end_time': l.endtime}
                return_list.append(lecturer_info)
        elif(block == 'G'):
            obj = Group.objects.get(pk=block_id)
            for d in days_py:
                g = GroupBlockedTimeslots.objects.create(
                    group=obj,
                    day=d,
                    starttime=start_time,
                    endtime=end_time
                )
                group_info = {'id': g.group.id, 'name': g.group.generated_group,
                              'day': g.day, 'start_time': g.starttime, 'end_time': g.endtime}
                return_list.append(group_info)
        elif(block == 'S'):
            obj = Subgroup.objects.get(pk=block_id)
            for d in days_py:
                g = GroupBlockedTimeslots.objects.create(
                    group=obj.group,
                    subgroup=obj,
                    day=d,
                    starttime=start_time,
                    endtime=end_time
                )
                subgroup_info = {'id': g.subgroup.id, 'name': g.subgroup.generated_subgroup,
                                 'day': g.day, 'start_time': g.starttime, 'end_time': g.endtime}
                return_list.append(subgroup_info)
        else:
            obj = Session1.objects.get(pk=block_id)
            for d in days_py:
                SessionBlockedTimeslots.objects.create(
                    session=obj,
                    day=d,
                    starttime=start_time,
                    endtime=end_time
                )

        timeobj = WorkingDays.objects.get()
        start_time = datetime.strptime(timeobj.starttime, '%H:%M')
        end_time = datetime.strptime(timeobj.endtime, '%H:%M')
        day_list = timeobj.get_all_days()
        time_arr = []

        if(timeobj.slot == '30 min slots'):
            time_arr = get_time_range(start_time, end_time, 30)
        else:
            time_arr = get_time_range(start_time, end_time, 60)

        data = {
            'success_stat': 1,
            'blocks': return_list,
            'day_list': day_list
        }
        return JsonResponse(data)
    except Exception as e:
        data = {
            'success_stat': 0
        }
        return JsonResponse(data)


def view_blocked_timeslots(request):
    try:
        block = request.GET.get('block', None)
        block_id = request.GET.get('block_id', None)
        obj = {}
        return_list = []

        if(block == 'L'):
            obj = Lecturer1.objects.get(pk=block_id)
            lobjs = LecturerBlockedTimeslots.objects.filter(lecturer=obj)
            for l in lobjs:
                lecturer_info = {'id': l.lecturer.employee_id, 'name': l.lecturer.name,
                                 'day': l.day, 'start_time': l.starttime, 'end_time': l.endtime}
                return_list.append(lecturer_info)
        elif(block == 'G'):
            obj = Group.objects.get(pk=block_id)
            group_objs = GroupBlockedTimeslots.objects.filter(group=obj)
            for g in group_objs:
                group_info = {'id': g.group.id, 'name': g.group.generated_group,
                              'day': g.day, 'start_time': g.starttime, 'end_time': g.endtime}
                return_list.append(group_info)
        elif(block == 'S'):
            obj = Subgroup.objects.get(pk=block_id)
            subgroup_objs = GroupBlockedTimeslots.objects.exclude(
                subgroup=None).filter(subgroup=obj)
            for g in subgroup_objs:
                subgroup_info = {'id': g.subgroup.id, 'name': g.subgroup.generated_subgroup,
                                 'day': g.day, 'start_time': g.starttime, 'end_time': g.endtime}
                return_list.append(subgroup_info)

        timeobj = WorkingDays.objects.get()
        start_time = datetime.strptime(timeobj.starttime, '%H:%M')
        end_time = datetime.strptime(timeobj.endtime, '%H:%M')
        day_list = timeobj.get_all_days()
        time_arr = []

        if(timeobj.slot == '30 min slots'):
            time_arr = get_time_range(start_time, end_time, 30)
        else:
            time_arr = get_time_range(start_time, end_time, 60)
        data = {
            'success_stat': 1,
            'blocks': return_list,
            'time_list': time_arr,
            'day_list': day_list
        }
        return JsonResponse(data)
    except Exception as e:
        data = {
            'success_stat': 0,
            'error_msg': 'Unexpected Error'
        }
        print(e)
        return JsonResponse(data)


def get_time_range(start_time, end_time, time_interval):
    time_arr = []
    current_time = start_time
    while (current_time < end_time):
        stime = current_time.strftime('%H:%M')
        time_arr.append(stime)
        current_time += datetime.timedelta(minutes=time_interval)

    time_arr.append(end_time.strftime('%H:%M'))
    return time_arr


#########################################################################################
# ranul


def addBuilding(request):
    return render(request, 'locations/add_building.html')


class CreateBuilding(View):
    def get(self, request):
        try:
            name = request.GET.get('name', None)

            obj = BuildingModel.objects.create(
                name=name,
            )

            building = {'id': obj.id, 'name': obj.name}

            data = {
                'building': building
            }

            return JsonResponse(data)

        except:
            pass


class CreateRoom(View):
    def get(self, request):
        try:
            name = request.GET.get('room_name', None)
            capacity = request.GET.get('capacity', None)
            room_type = request.GET.get('type', None)
            bid = request.GET.get('id', None)

            building = BuildingModel.objects.get(id=bid)

            obj = RoomModel.objects.create(
                name=name,
                capacity=capacity,
                room_type=room_type,
                building=building,
            )

            room = {'id': obj.id, 'name': obj.name}

            data = {
                'room': room
            }

            return JsonResponse(data)

        except:
            print("fail adding data")
            pass


class DeleteBuilding(View):
    try:
        def get(self, request):
            id = request.GET.get('id', None)
            BuildingModel.objects.get(id=id).delete()
            data = {
                'deleted': True
            }
            return JsonResponse(data)
    except:

        print("lecturer delete failed")
        pass


class DeleteRoom(View):
    try:
        def get(self, request):
            id = request.GET.get('id', None)
            RoomModel.objects.get(id=id).delete()
            data = {
                'deleted': True
            }
            return JsonResponse(data)
    except:
        pass


class UpdateBuilding(View):
    try:
        def get(self, request):
            id = request.GET.get('id', None)
            name = request.GET.get('name', None)

            obj = BuildingModel.objects.get(id=id)
            obj.name = name
            obj.save()

            lecturer = {'id': obj.id, 'name': obj.name}

            data = {
                'lecturer': lecturer
            }
            return JsonResponse(data)

    except:

        print("lecturer update failed")
        pass


class UpdateRoom(View):
    try:
        def get(self, request):
            id = request.GET.get('id', None)
            name = request.GET.get('room_name', None)
            capacity = request.GET.get('capacity', None)
            room_type = request.GET.get('type', None)

            obj = RoomModel.objects.get(id=id)
            obj.name = name
            obj.capacity = capacity
            obj.room_type = room_type
            obj.save()

            room = {'id': obj.id, 'name': obj.name}

            data = {
                'room': room
            }
            return JsonResponse(data)

    except:

        print("lecturer update failed")
        pass


class Buildings(ListView):
    model = BuildingModel
    template_name = 'locations/all_buildings.html'
    context_object_name = 'buildings'


class BuildingDetail(DetailView):
    model = BuildingModel
    template_name = 'locations/building_detail.html'


def lecturerStatistics(request):
    return render(request, 'statistics/lecturer_statistics.html')


def lecturerCount(reuqest):
    count = Lecturer1.objects.count()
    data = {
        'count': count
    }
    return JsonResponse(data)


def lecturerCenterStats(request):
    metro = Lecturer1.objects.filter(center='Metro').count()
    malabe = Lecturer1.objects.filter(center='Malabe').count()
    matara = Lecturer1.objects.filter(center='Matara').count()
    kurunegala = Lecturer1.objects.filter(center='Kurunagala').count()
    kandy = Lecturer1.objects.filter(center='Kandy').count()
    jaffna = Lecturer1.objects.filter(center='Jaffna').count()
    centers = [metro, malabe, matara, kurunegala, kandy, jaffna]
    data = {
        'centers': centers,
    }
    return JsonResponse(data)


def lecurerLevelStat(request):
    p = Lecturer1.objects.filter(level=1).count()
    ap = Lecturer1.objects.filter(level=2).count()
    slhg = Lecturer1.objects.filter(level=3).count()
    sl = Lecturer1.objects.filter(level=4).count()
    l = Lecturer1.objects.filter(level=5).count()
    al = Lecturer1.objects.filter(level=6).count()
    i = Lecturer1.objects.filter(level=7).count()
    levels = [p, ap, slhg, sl, l, al, i]
    data = {
        'levels': levels
    }
    return JsonResponse(data)


def subjectCount(request):
    count = Subjects1.objects.count()
    data = {
        'count': count
    }
    return JsonResponse(data)


def subjectStatistics(request):
    return render(request, 'statistics/subject_statistics.html')


def allSubjectStatistics(request):
    subjects = Subjects1.objects.all()
    return JsonResponse(serializers.serialize('json', subjects), safe=False)


def studentStatistics(request):
    return render(request, 'statistics/student_statistics.html')


def allProgrammeStatistics(request):
    programmes = Programme.objects.all()
    return JsonResponse(serializers.serialize('json', programmes), safe=False)


def allYearSemesterStatistics(request):
    yearSemester = AcademicYearSemester.objects.all()
    return JsonResponse(serializers.serialize('json', yearSemester), safe=False)


def allGroupStatistics(request):
    groups = Group.objects.all()
    return JsonResponse(serializers.serialize('json', groups), safe=False)


def allSubGroupStatistics(request):
    subGroups = Subgroup.objects.all()
    return JsonResponse(serializers.serialize('json', subGroups), safe=False)


def statistics(request):
    return render(request, 'statistics/statistics.html')

# rooms for lecturers view


def lecturerRooms(request):
    return render(request, 'rooms/lecturers.html')

# load lecturers


def loadLecturers(request):
    return JsonResponse(serializers.serialize('json', Lecturer1.objects.all(), fields=('name')), safe=False)

# load all rooms with building names


def loadRooms(request):
    locations = RoomModel.objects.select_related(
        'building').order_by('building')
    list = []
    for row in locations:
        list.append(
            {'building_name': row.building.name, 'building_id': row.building.id, 'room_name': row.name, 'room_id': row.id})
    return JsonResponse(list, safe=False)

# rooms for groups


def groupRooms(request):
    return render(request, 'rooms/groups.html')

# rooms for sessions


def sessionRooms(request):
    return render(request, 'rooms/sessions.html')

# rooms for consecutive sessions


def consecutiveSessionRooms(request):
    some()
    return render(request, 'rooms/consecutive_sessions.html')


def some():
    try:
        print('lol')
        print(datetime.timedelta(hours=2))
        va = WorkingDays.objects.all()
        days = va[0].days
        v = []
        v = days.split(',')
        print(v)
        # for index, i in enumerate(v):
        #     if i == 'tuesday':
        #         v[index] = 2
        # print(v)

        gid = 68
        st = 8
        et = 5

        sessions = Session.objects.filter(group_id_id=gid)
        sessionids = []
        for i in sessions:
            sessionids.append(i.id)

        print(sessionids)

        blockedtimes = GroupBlockedTimeslots.objects.filter(
            group_id=gid)

        print('#########')
        s = '18:00'

        datetime_object = datetime.strptime(
            'Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
        print(datetime_object)

        # for i in sessions:
        #     end = st + i.duration
        #     for k in v:
        #         for j in blockedtimes:
        #             if(j.day != k and st > j.endtime and end < j.starttime):
        #                 print('ok'+i.id)

        print(sessionids)
        return HttpResponse(' ')
    except:
        pass

# rooms for subjects and relevant tags


def subjectRooms(request):
    return render(request, 'rooms/subjects.html')

# unavailable times of rooms


def timeRooms(request):
    return render(request, 'rooms/time.html')


# rooms for tags


def tagRooms(request):
    return render(request, 'rooms/tags.html')

# add unavailable times of rooms


class addUnavailableRooms(View):
    def get(self, request):
        try:
            day = request.GET.get('day', None)
            start = request.GET.get('start', None)
            end = request.GET.get('end', None)
            building = request.GET.get('building', None)
            room = request.GET.get('room', None)

            obj = UnavailableRoom.objects.create(
                day=day,
                start_time=start,
                end_time=end,
                building_id=building,
                room_id=room,
            )

            saved = {
                'id': obj.id
            }

            data = {
                'created': saved
            }

            return JsonResponse(data)

        except:
            pass

# delete all unavailable rooms


def deleteAllUnavailableRooms(request):
    try:
        UnavailableRoom.objects.all().delete()
        return HttpResponse('')
    except:
        pass

# delete unavailable room


def deleteUnavailableRoom(request):
    try:
        id = request.GET.get('id', None)
        UnavailableRoom.objects.get(id=id).delete()
        data = {
            'created': True
        }
        return JsonResponse(data)
    except:
        pass

# add rooms for lecturers


class addLecturerRooms(View):
    def get(self, request):
        try:
            lec = request.GET.get('lec', None)
            building = request.GET.get('building', None)
            room = request.GET.get('room', None)

            obj = LecturerRoom.objects.create(
                lecturer_id=lec,
                building_id=building,
                room_id=room
            )

            data = {
                'id': obj.id
            }
            return JsonResponse(data)
        except:
            pass

# delete rooms for lecturers


def deleteLecturerRooms(request):
    try:
        id = request.GET.get('id', None)
        LecturerRoom.objects.get(id=id).delete()
        data = {
            'created': True
        }
        return JsonResponse(data)
    except:
        pass

# delete all rooms for lecturers


def deleteAllLecturerRooms(request):
    try:
        LecturerRoom.objects.all().delete()
        return HttpResponse('')
    except:
        pass

# load groups


def loadGroups(request):
    return JsonResponse(serializers.serialize('json', Group.objects.all(), fields=('generated_group')), safe=False)


def loadSubGroups(request):
    return JsonResponse(serializers.serialize('json', Subgroup.objects.all(), fields=('generated_subgroup')), safe=False)


# add rooms for groups

def addGroupRoom(request):
    try:
        group = request.GET.get('group', None)
        building = request.GET.get('building', None)
        room = request.GET.get('room', None)

        obj = GroupRoom.objects.create(
            group_id=group, building_id=building, room_id=room
        )

        data = {
            'id': obj.id
        }

        return JsonResponse(data)

    except:
        pass

# add rooms for sub groups


def addSubGroupRoom(request):
    try:
        subgroup = request.GET.get('subgroup', None)
        building = request.GET.get('building', None)
        room = request.GET.get('room', None)

        obj = SubGroupRoom.objects.create(
            subgroup_id=subgroup, building_id=building, room_id=room
        )

        data = {
            'id': obj.id
        }

        return JsonResponse(data)

    except:
        pass


# delete group room
def deleteGroupRooms(request):
    try:
        id = request.GET.get('id', None)
        GroupRoom.objects.get(id=id).delete()
        data = {
            'created': True
        }
        return JsonResponse(data)
    except:
        pass


# delete subgroup room
def deleteSubGroupRooms(request):
    try:
        id = request.GET.get('id', None)
        SubGroupRoom.objects.get(id=id).delete()
        data = {
            'created': True
        }
        return JsonResponse(data)
    except:
        pass

# delete all groups and subgroup rooms


def deleteAllGroupRooms(request):
    try:
        GroupRoom.objects.all().delete()
        SubGroupRoom.objects.all().delete()
        return HttpResponse('')
    except:
        pass

# load tags


def loadTags(request):
    return JsonResponse(serializers.serialize('json', Tags.objects.all(), fields=('label')), safe=False)


def addTagRoom(request):
    try:
        tag = request.GET.get('tag', None)
        building = request.GET.get('building', None)
        room = request.GET.get('room', None)

        obj = TagRoom.objects.create(
            tag_id=tag, building_id=building, room_id=room
        )

        data = {
            'id': obj.id
        }

        return JsonResponse(data)
    except:
        pass

# delete tag room


def deleteTagRoom(request):
    try:
        id = request.GET.get('id', None)
        TagRoom.objects.get(id=id).delete()
        data = {
            'created': True
        }
        return JsonResponse(data)
    except:
        pass


# delete all tag rooms


def deleteAllTagRooms(request):
    try:
        TagRoom.objects.all().delete()
        return HttpResponse('')
    except:
        pass


# load subjects
def loadSubjects(request):
    return JsonResponse(serializers.serialize('json', Subjects1.objects.all(), fields=('subjectName')), safe=False)


# add rooms for subject and tag
def addSubjectTagRoom(request):
    try:
        subject = request.GET.get('subject', None)
        tag = request.GET.get('tag', None)
        building = request.GET.get('building', None)
        room = request.GET.get('room', None)

        obj = SubjectTagRoom.objects.create(
            subject_id=subject, tag_id=tag, building_id=building, room_id=room
        )

        data = {
            'id': obj.id
        }

        return JsonResponse(data)
    except:
        pass


def deleteSubjectTagRoom(request):
    try:
        id = request.GET.get('id', None)
        SubjectTagRoom.objects.get(id=id).delete()
        data = {
            'created': True
        }
        return JsonResponse(data)
    except:
        pass


def deleteAllSubjectTagRooms(request):
    try:
        SubjectTagRoom.objects.all().delete()
        return HttpResponse('')
    except:
        pass

# load all sessions


def loadGroupSessions(request):
    locations = Session.objects.select_related(
        'group_id').select_related('tag').select_related('subject')
    list = []
    for row in locations:
        list.append(
            {'group_name': row.group_id.generated_group, 'id': row.id, 'tag': row.tag.label, 'subject': row.subject.subjectName})
    return JsonResponse(list, safe=False)


# load all subgroup sessions

def loadSubGroupSessions(request):
    locations = Session.objects.filter(subgroup_id__isnull=False).select_related(
        'subgroup_id').select_related('tag').select_related('subject')
    list = []
    for row in locations:
        list.append(
            {'group_name': row.subgroup_id.generated_subgroup, 'id': row.id, 'tag': row.tag.label, 'subject': row.subject.subjectName})
    return JsonResponse(list, safe=False)

# add rooms for sessions


def addSessionRooms(request):
    try:
        session = request.GET.get('session', None)
        building = request.GET.get('building', None)
        room = request.GET.get('room', None)

        obj = SessionRoom.objects.create(
            session_id=session, building_id=building, room_id=room
        )

        data = {
            'id': obj.id
        }

        return JsonResponse(data)
    except:
        pass


# delete session rooms
def deleteSessionRooms(request):
    try:
        id = request.GET.get('id', None)
        SessionRoom.objects.get(id=id).delete()
        data = {
            'created': True
        }
        return JsonResponse(data)
    except:
        pass


def deleteAllSessionRooms(request):
    try:
        SessionRoom.objects.all().delete()
        return HttpResponse('')
    except:
        pass


# load saved session rooms
def loadConsecutiveSessions(request):
    locations = ConsecutiveSession.objects.select_related(
        'session1').select_related('session2')
    list = []
    for row in locations:
        list.append(
            {'session1_subject': row.session1.subject.subjectName, 'session1_tag': row.session1.tag.label, 'session1_group': row.session1.group_id.generated_group, 'session2_subject': row.session2.subject.subjectName, 'session2_tag': row.session2.tag.label, 'session2_group': row.session2.group_id.generated_group})

    # print(list)
    return JsonResponse(list, safe=False)


# ranul
#########################################################################################
