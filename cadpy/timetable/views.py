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

class DDView(generic.ListView):
    model = Tags
    template_name = 'students/st.html'


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

class StudentsGenerationView(generic.ListView):
    context_object_name  = 'group_list'
    
    def get_queryset(self):
        """Return the last five published questions."""
        listOfGroups = Group.objects.filter(generated_group = None)
        for group in listOfGroups:
            print(group.pk)
            #group_obj = Group.objects.get(pk=group.pk)
            group_id = group.generate_group_id()
            group.generated_group = group_id
            group.save()
        return Group.objects.exclude(generated_group = None)

    template_name = 'students/students.html'

class StudentsSubGroupGenerationView(generic.ListView):
    context_object_name  = 'group_list'
    
    def get_queryset(self):
        """Return the last five published questions."""
        groupy = Group.objects.get(id = 27)
        for subgroup in groupy.subgroup_set.all():
            print(subgroup.pk)
            #group_obj = Group.objects.get(pk=group.pk)
            subgroup_id = subgroup.generate_subgroup_id()
            subgroup.generated_subgroup = subgroup_id
            subgroup.save()
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
                'success_stat': 1,
                'programme': programme
            }
            print("successfull")

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
    def  get(self, request):
        try:
            id1 = request.GET.get('id', None)
            pname = request.GET.get('programme_name', None)
            pabbv = request.GET.get('programme_abbv', None)

            obj = Programme.objects.get(id=id1)
            obj.programme_name = pname
            obj.programme_abbv = pabbv
            obj.save()
            programme = {'id':obj.id,'programme_name':obj.programme_name,'programme_abbv':obj.programme_abbv}
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
    def  get(self, request):
        
        try:
            ayear = request.GET.get('academic_year', None)
            asemester = request.GET.get('academic_semester', None)
            obj = AcademicYearSemester.objects.create(
                academic_year=ayear,
                academic_semester=asemester
            )
            
            academicyearsemester = {'id': obj.id, 'academic_year': obj.academic_year, 'academic_semester': obj.academic_semester }
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
    def  get(self, request):
        try:
            id1 = request.GET.get('id', None)
            ayear = request.GET.get('academic_year', None)
            asemester = request.GET.get('academic_semester', None)

            obj = AcademicYearSemester.objects.get(id=id1)
            obj.academic_year = ayear
            obj.academic_semester = asemester
            obj.save()
            academicyearsemester = {'id':obj.id ,'academic_year':obj.academic_year ,'academic_semester':obj.academic_semester}
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
    context_object_name  = 'group_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['programme_ll'] = Programme.objects.all()
        context['academic_ll'] = AcademicYearSemester.objects.all()
        return context
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Group.objects.filter(generated_group = None)
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
    def  get(self, request):
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
            group = {'id': obj.id, 'group_no': obj.group_no, 'student_count': obj.student_count, 'academic_year': obj.academic_year_semester.academic_year, 'academic_semester': obj.academic_year_semester.academic_semester, 'programme': obj.programme.programme_abbv}
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
        
class AddSubGroups(View):
    def  get(self, request, pk):
        
        try:
            gp = request.GET.get('group', None)
            subgp = request.GET.get('subgroup_no', None)
            print(gp)
            print(subgp)
            groupObj = Group.objects.get(pk=pk)
            print(groupObj)
            obj = Subgroup.objects.create(
                group = groupObj,
                subgroup_no=subgp,
            )
            print('created')
            subgroup = {'id': obj.id, 'group': obj.group.generated_group, 'group_id': obj.group.id, 'subgroup_no': obj.subgroup_no }
            data = {
                'subgroup': subgroup
            }
            print("successfull")

            return JsonResponse(data)

        except:
            print("fail adding data")
            pass   

class DeleteSubGroups(View):
    try:
        def  get(self, request, pk):
            id1 = request.GET.get('id', None)
           
            Subgroup.objects.get(id=id1).delete()
            
            data = {
                'deleted': True
            }
            return JsonResponse(data)
    except:
        
        print("programme delete failed")
        pass


class UpdateSubGroupsView(View):
    try:
        def  get(self, request, pk):
            id1 = request.GET.get('id', None)
            pabbv = request.GET.get('subgroup_no', None)

            obj = Subgroup.objects.get(id=id1)
            obj.subgroup_no = pabbv
            obj.save()
            subgroup = {'id':obj.id,'subgroup_no':obj.subgroup_no}
            data = {
                'subgroup': subgroup
            }
            return JsonResponse(data)    
    except:
        print("subgroup update failed")
        pass        