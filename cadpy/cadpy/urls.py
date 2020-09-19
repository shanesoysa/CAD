"""cadpy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from timetable import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('lecturer/',  views.Lecturer.as_view(), name='lecturer'),
    path('lecturer/addlec/',  views.AddLecturer.as_view(), name='lecturer_create'),
    path('lecturer/updatelec/',  views.UpdateLecturer.as_view(), name='lecturer_update'),
    path('lecturer/deletelec/', views.DeleteLecturer.as_view(), name='lecturer_delete'),

    
    path('subjects/',  views.Subjects.as_view(), name='subject'),
    path('subjects/addsubject/',  views.AddSubjects.as_view(), name='subject_create'),
    path('subjects/updatesubject/',  views.UpdateSubject.as_view(), name='subject_update'),
    path('subjects/deletesubject/', views.DeleteSubject.as_view(), name='subject_delete'),

    path('programmes/', views.ProgrammesView.as_view() , name='programmes'),
    path('programmes/add', views.AddProgramme.as_view() , name='add_programmes'),
    path('programmes/delete', views.DeleteProgramme.as_view() , name='remove_programmes'),
    path('programmes/update', views.UpdateProgramme.as_view() , name='update_programmes'),
    
    path('academics/', views.AcademicYearSemesterView.as_view() , name='academics'),
    path('academics/add', views.AddAcademicYearSemesterView.as_view() , name='add_academics'),
    path('academics/delete', views.DeleteAcademicYearSemesterView.as_view() , name='remove_academics'),
    path('academics/update', views.UpdateAcademicYearSemesterView.as_view() , name='update_academics'),
   
   
    path('<int:pk>/subgroups', views.SubGroupsView.as_view() , name='subgroups'),
    path('<int:pk>/subgroups/add', views.AddSubGroups.as_view() , name='add_subgroups'),
    path('<int:pk>/subgroups/delete', views.DeleteSubGroups.as_view() , name='remove_subgroups'),
    path('<int:pk>/subgroups/update', views.UpdateSubGroupsView.as_view() , name='update_subgroups'),
    path('<int:pk>/subgroups/generate', views.StudentsSubGroupGenerationView.as_view() , name='generate_subgroups'),


    path('dd/', views.DDView.as_view(), name='dd'),


    path('students/', views.StudentsView.as_view(), name='students'),
    path('students/generate', views.StudentsGenerationView.as_view(), name='generate_students'),


    path('tags/', views.TagsView.as_view() , name='tags'),
    path('tags/add', views.AddTagsView.as_view() , name='add_tags'),
    path('tags/delete', views.DeleteTags.as_view() , name='remove_tags'),
    path('tags/update', views.UpdateTags.as_view() , name='update_tags'),

    path('groups/', views.GroupsView.as_view() , name='groups'),
    path('groups/add', views.AddStudentsView.as_view() , name='add_groups'),
    path('groups/delete', views.DeleteStudentsView.as_view() , name='remove_groups'),
    path('groups/update', views.UpdateGroupsView.as_view() , name='update_groups'),

    path('sessions/assign', views.AssignSessionsView.as_view(), name="assign_sessions"),
    path('timeslots/blocked', views.BlockTimeSlotsView.as_view(), name="blocked_timeslots"),
    path('sessions/consecutive', views.ConsecutiveSessionsView.as_view(), name="consecutive_sessions")
]
