from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import View
from django.http import JsonResponse
from .models import Lecturer as Lecturer1

# Create your views here.

class Lecturer(ListView):
    model = Lecturer1
    template_name = 'list_lecturers.html'
    context_object_name = 'lecturers'




class AddLecturer(View):
    def  get(self, request):
        
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
            

            lecturer = {'id':obj.id,'name':obj.name,'center':obj.center,'employee_id':obj.employee_id,'building':obj.building,'faculty':obj.faculty,'level':obj.level,'department':obj.department,'rank':obj.rank}

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
        def  get(self, request):
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

            lecturer = {'id':obj.id,'name':obj.name,'center':obj.center,'employee_id':obj.employee_id,'building':obj.building,'faculty':obj.faculty,'level':obj.level,'department':obj.department,'rank':obj.rank}

            data = {
                'lecturer': lecturer
            }
            return JsonResponse(data)
            
    except:
        
        print("lecturer update failed")
        pass
    

class DeleteLecturer(View):
    try:
        def  get(self, request):
            id1 = request.GET.get('id', None)
            Lecturer1.objects.get(id=id1).delete()
            data = {
                'deleted': True
            }
            return JsonResponse(data)
    except:
        
        print("lecturer delete failed")
        pass
        