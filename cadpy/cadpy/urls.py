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
    path('',  views.Lecturer.as_view(), name='lecturer'),
    path('addlec/',  views.AddLecturer.as_view(), name='lecturer_create'),
    path('updatelec/',  views.UpdateLecturer.as_view(), name='lecturer_update'),
    path('deletelec/', views.DeleteLecturer.as_view(), name='lecturer_delete'),

    path('programmes/', views.ProgrammesView.as_view() , name='programmes'),
    path('programmes/add', views.AddProgramme.as_view() , name='add_programmes'),
    path('programmes/delete', views.DeleteProgramme.as_view() , name='remove_programmes'),
    path('programmes/update', views.UpdateProgramme.as_view() , name='update_programmes'),
    
    path('academics/', views.AcademicYearSemesterView.as_view() , name='academics'),
    path('academics/add', views.AddAcademicYearSemesterView.as_view() , name='add_academics'),
    path('academics/delete', views.DeleteAcademicYearSemesterView.as_view() , name='remove_academics'),
    path('academics/update', views.UpdateAcademicYearSemesterView.as_view() , name='update_academics'),
   
   
    path('<int:pk>/subgroups', views.UpdateAcademicYearSemesterView.as_view() , name='subgroups'),

    path('students/', views.StudentsView.as_view(), name='students'),
    path('students/', views.StudentsView.as_view(), name='students'),
    path('students/delete', views.UpdateAcademicYearSemesterView.as_view(), name='remove_students'),


    path('tags/', views.TagsView.as_view() , name='tags'),
    path('tags/add', views.AddTagsView.as_view() , name='add_tags'),
    path('tags/delete', views.DeleteTags.as_view() , name='remove_tags'),
    path('tags/update', views.UpdateTags.as_view() , name='update_tags'),

    path('groups/', views.GroupsView.as_view() , name='groups'),
    path('groups/add', views.AddStudentsView.as_view() , name='add_groups'),
    path('groups/delete', views.DeleteStudentsView.as_view() , name='remove_groups'),
    path('groups/update', views.UpdateGroupsView.as_view() , name='update_groups'),


]
