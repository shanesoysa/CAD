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
    # path('',  views.Lecturer.as_view(), name='lecturer'),
    path('addlec/',  views.AddLecturer.as_view(), name='lecturer_create'),
    path('updatelec/',  views.UpdateLecturer.as_view(), name='lecturer_update'),
    path('deletelec/', views.DeleteLecturer.as_view(), name='lecturer_delete'),
    # path('building2/', views.addBuilding2, name='building2'),
    # path('all_buildings2', views.allBuildings2, name='all_buildings2'),
    path('', views.home, name='home'),
    #####################################################
    # ranul
    # location
    path('building/', views.addBuilding, name='building'),
    path('building/building_create/',
         views.CreateBuilding.as_view(), name='add_building'),
    path('building/delete_building/',
         views.DeleteBuilding.as_view(), name='delete_building'),
    path('building/update_building/',
         views.UpdateBuilding.as_view(), name='update_building'),
    path('building/add_room/', views.CreateRoom.as_view(), name='add_room'),
    path('building/delete_room/', views.DeleteRoom.as_view(), name='delete_room'),
    path('building/update_room/', views.UpdateRoom.as_view(), name='update_room'),
    path('all_buildings', views.Buildings.as_view(), name='all_buildings'),
    path('building/<int:pk>/', views.BuildingDetail.as_view(),
         name='building_detail'),
    # statistics
    path('lecturer_statistics', views.lecturerStatistics,
         name='lecturer_statistics'),
    path('subject_statistics', views.subjectStatistics, name='subject_statistics'),
    path('student_statistics', views.studentStatistics, name='student_statistics'),
    path('statistics', views.statistics, name='statistics'),
    #####################################################
]
