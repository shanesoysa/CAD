from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import View
from django.views import generic
from django.http import JsonResponse
from .models import Lecturer as Lecturer1, Subgroup, Group, Programme, AcademicYearSemester, Tags

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


#Rehani's    
class TagsView(generic.ListView):
    model = Tags
    template_name = 'tags/tags.html'


class DeleteTags(View):
    try:
        def  get(self, request):
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
    def  get(self, request):
        try:
            pname = request.GET.get('label', None)
            pabbv = request.GET.get('color', None)
            obj = Tags.objects.create(
                label=pname,
                color=pabbv
            )
            tags = {'id': obj.id, 'label': obj.label, 'color': obj.color }
            data = {
                'tags': tags
            }
            return JsonResponse(data)
        except:
            print("fail adding data")
            pass   

class UpdateTags(View):
    try:
        def  get(self, request):
            id1 = request.GET.get('id', None)
            pname = request.GET.get('label', None)
            pabbv = request.GET.get('color', None)

            obj = Tags.objects.get(id=id1)
            obj.label = pname
            obj.color = pabbv
            obj.save()
            tags = {'id':obj.id, 'label':obj.label, 'color':obj.color}
            data = {
                'tags': tags
            }
            return JsonResponse(data)    
    except:
        print("tags update failed")
        pass


class StudentsView(generic.ListView):
    context_object_name  = 'group_list'
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Group.objects.exclude(generated_group = None)
    template_name = 'students/students.html'

class ProgrammesView(generic.ListView):
    model = Programme
    template_name = 'students/programmes.html'

class AddProgramme(View):
    def  get(self, request):
        
        try:
            pname = request.GET.get('programme_name', None)
            pabbv = request.GET.get('programme_abbv', None)
            print(pname)
            print(pabbv)
            obj = Programme.objects.create(
                programme_name=pname,
                programme_abbv=pabbv
            )
            programme = {'id': obj.id, 'programme_name': obj.programme_name, 'programme_abbv': obj.programme_abbv }
            data = {
                'programme': programme
            }
            print("successfull")

            return JsonResponse(data)

        except:
            print("fail adding data")
            pass   

class DeleteProgramme(View):
    try:
        def  get(self, request):
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
    try:
        def  get(self, request):
            id1 = request.GET.get('id', None)
            pname = request.GET.get('programme_name', None)
            pabbv = request.GET.get('programme_abbv', None)

            obj = Programme.objects.get(id=id1)
            obj.programme_name = pname
            obj.programme_abbv = pabbv
            obj.save()
            programme = {'id':obj.id,'programme_name':obj.programme_name,'programme_abbv':obj.programme_abbv}
            data = {
                'programme': programme
            }
            return JsonResponse(data)    
    except:
        print("programme update failed")
        pass

class AcademicYearSemesterView(generic.ListView):
    model = AcademicYearSemester
    template_name = 'students/academic-year-semester.html'


class AddAcademicYearSemesterView(View):
    def  get(self, request):
        
        try:
            ayear = request.GET.get('academic_year', None)
            asemester = request.GET.get('academic_semester', None)
            print(ayear)
            print(asemester)
            obj = AcademicYearSemester.objects.create(
                academic_year=ayear,
                academic_semester=asemester
            )
            academicyearsemester = {'id': obj.id, 'academic_year': obj.academic_year, 'academic_semester': obj.academic_semester }
            data = {
                'academicyearsemester': academicyearsemester
            }
            print("successfull")
            return JsonResponse(data)
        except:
            print("fail adding data")
            pass   

class DeleteAcademicYearSemesterView(View):
    try:
        def  get(self, request):
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
    try:
        def  get(self, request):
            id1 = request.GET.get('id', None)
            ayear = request.GET.get('academic_year', None)
            asemester = request.GET.get('academic_semester', None)

            obj = AcademicYearSemester.objects.get(id=id1)
            obj.academic_year = ayear
            obj.academic_semester = asemester
            obj.save()
            academicyearsemester = {'id':obj.id ,'academic_year':obj.academic_year ,'academic_semester':obj.academic_semester}
            data = {
                'academicyearsemester': academicyearsemester
            }
            return JsonResponse(data)    
    except:
        print("Academic year-semester update failed")
        pass



class GroupsView(generic.ListView):
    model = Group
    template_name = 'students/generate-groups.html'



class AddStudentsView(View):
    def  get(self, request):
        
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
            student = {'id': obj.id, 'group_no': obj.group_no, 'student_count': obj.student_count, 'academic_year': obj.academic_year_semester.academic_year, 'academic_semester': obj.academic_year_semester.academic_semester, 'programme': obj.programme.programme_abbv}
            data = {
                'student': student
            }
            print("successfull")
            return JsonResponse(data)
        except:
            print("fail adding data")
            pass   


class UpdateGroupsView(View):
    try:
        def  get(self, request):
            id1 = request.GET.get('id', None)
            academics = request.GET.get('academic_year_semester', None)
            gprogramme = request.GET.get('programme', None)
            ggroup = request.GET.get('group_no', None)
            scount = request.GET.get('student_count', None)

            obj = Group.objects.get(id=id1)
            obj.academic_year_semester = academics
            obj.programme = programme
            obj.group_no = ggroup
            obj.student_count = scount
            obj.save()
            group = {'id':obj.id ,'academic_year_semester':obj.academic_year_semester ,'programme':obj.programme, 'group_no': obj.group_no, 'student_count': student_count }
            data = {
                'group': group
            }
            return JsonResponse(data)    
    except:
        print("update of group failed")
        pass

class DeleteStudentsView(View):
    try:
        def  get(self, request):
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
        