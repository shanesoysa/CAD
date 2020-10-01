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
from django.urls import path,include
from timetable import views


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('side/', views.side, name='side'),
    path('lec/',  views.Lecturer.as_view(), name='lecturer'),
    path('workingdays/',views.Workingdays.as_view(),name='Workingdays'),
    path('adddays/',views.Adddays.as_view(),name='workingdays_create'),
    path('updatedays/',views.Updatedays.as_view(),name='workingdays_update'),
    path('deletedays/',views.Deletedays.as_view(),name='workingdays_delete'),
    path('addlec/',  views.AddLecturer.as_view(), name='lecturer_create'),
    path('updatelec/',  views.UpdateLecturer.as_view(), name='lecturer_update'),
    path('deletelec/', views.DeleteLecturer.as_view(), name='lecturer_delete'),
    path('timetables/', views.timetables,name='timetable')
]

