from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import View
from django.http import JsonResponse
from .models import Lecturer as Lecturer1
from .models import WorkingDays 
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
        


def side(request):
    return render(request,'side.html')



class Workingdays(ListView):
    model = WorkingDays
    template_name = 'addDays.html'
    context_object_name = 'days'
    print(model)



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
                 #print(y)
                 #print("successfull")
            obj = WorkingDays.objects.create(
                     nubdays=ndays,
                     days=workingdays,
                     starttime=stime,
                     endtime=etime,
                     slot=slots,
                     )

            day = {'id':obj.id,'nubdays':obj.nubdays,'days':obj.days,'starttime':obj.starttime,'endtime':obj.endtime,'slot':obj.slot}
            data = {
                     'day': day
                      }
                 #print("successfull")
                 #print(data)
            return JsonResponse(data)
            
        except:
            
            print("fail adding data")
            pass 



            
        

class Updatedays(View):
    def get(self, request):
        
        try:
            id1=request.GET.get('id',None)
            ndays = request.GET.get('numdays', None)
            workingdays = request.GET.get('workingdays', None)
            stime = request.GET.get('stime', None)
            etime = request.GET.get('etime', None)
            slots = request.GET.get('slots', None)
           
            
            obj = WorkingDays.objects.get(id=id1)
            obj.nubdays=ndays
            obj.days=workingdays
            obj.starttime=stime
            obj.endtime=etime
            obj.slot=slots
            obj.save()
               
            
            

            day = {'id':obj.id,'nubdays':obj.nubdays,'days':obj.days,'starttime':obj.starttime,'endtime':obj.endtime,'slot':obj.slot}

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
    def  get(self, request):
        id1 = request.GET.get('id', None)
        WorkingDays.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


def timetables(request):
    return render(request, 'timetables.html')