from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import ListView
from django.views.generic import View, DetailView
from django.http import JsonResponse
from .models import AcademicYearSemester, Group, Lecturer as Lecturer1, Building as BuildingModel, Programme, Room as RoomModel, Subgroup
from .models import Subjects as Subjects1
from django.core import serializers

# Create your views here.


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


def home(request):
    return render(request, 'home.html')


#########################################################################################
# ranul


def addBuilding(request):
    return render(request, 'add_building.html')


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
            print('ddd')

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

        print("lecturer delete failed")
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
    template_name = 'all_buildings.html'
    context_object_name = 'buildings'


class BuildingDetail(DetailView):
    model = BuildingModel
    template_name = 'building_detail.html'


def lecturerStatistics(request):
    return render(request, 'lecturer_statistics.html')


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
    return render(request, 'subject_statistics.html')


def allSubjectStatistics(request):
    subjects = Subjects1.objects.all()
    return JsonResponse(serializers.serialize('json', subjects), safe=False)


def studentStatistics(request):
    return render(request, 'student_statistics.html')


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
    return render(request, 'statistics.html')

#########################################################################################
