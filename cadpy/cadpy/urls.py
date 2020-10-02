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
from os import name
from django.contrib import admin
from django.urls import path
from timetable import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('lecturer/',  views.Lecturer.as_view(), name='lecturer'),
    path('lecturer/addlec/',  views.AddLecturer.as_view(), name='lecturer_create'),
    path('lecturer/updatelec/',  views.UpdateLecturer.as_view(),
         name='lecturer_update'),
    path('lecturer/deletelec/', views.DeleteLecturer.as_view(),
         name='lecturer_delete'),


    path('subjects/',  views.Subjects.as_view(), name='subject'),
    path('subjects/addsubject/',  views.AddSubjects.as_view(), name='subject_create'),
    path('subjects/updatesubject/',
         views.UpdateSubject.as_view(), name='subject_update'),
    path('subjects/deletesubject/',
         views.DeleteSubject.as_view(), name='subject_delete'),

    path('programmes/', views.ProgrammesView.as_view(), name='programmes'),
    path('programmes/add', views.AddProgramme.as_view(), name='add_programmes'),
    path('programmes/delete', views.DeleteProgramme.as_view(),
         name='remove_programmes'),
    path('programmes/update', views.UpdateProgramme.as_view(),
         name='update_programmes'),

    path('academics/', views.AcademicYearSemesterView.as_view(), name='academics'),
    path('academics/add', views.AddAcademicYearSemesterView.as_view(),
         name='add_academics'),
    path('academics/delete', views.DeleteAcademicYearSemesterView.as_view(),
         name='remove_academics'),
    path('academics/update', views.UpdateAcademicYearSemesterView.as_view(),
         name='update_academics'),


    path('<int:pk>/subgroups', views.SubGroupsView.as_view(), name='subgroups'),
    path('<int:pk>/subgroups/add',
         views.AddSubGroups.as_view(), name='add_subgroups'),
    path('<int:pk>/subgroups/delete',
         views.DeleteSubGroups.as_view(), name='remove_subgroups'),
    path('<int:pk>/subgroups/update',
         views.UpdateSubGroupsView.as_view(), name='update_subgroups'),
    path('<int:pk>/subgroups/generate',
         views.StudentsSubGroupGenerationView.as_view(), name='generate_subgroups'),


    path('dd/', views.DDView.as_view(), name='dd'),


    path('students/', views.StudentsView.as_view(), name='students'),
    path('students/generate', views.StudentsGenerationView.as_view(),
         name='generate_students'),


    path('tags/', views.TagsView.as_view(), name='tags'),
    path('tags/add', views.AddTagsView.as_view(), name='add_tags'),
    path('tags/delete', views.DeleteTags.as_view(), name='remove_tags'),
    path('tags/update', views.UpdateTags.as_view(), name='update_tags'),

    path('groups/', views.GroupsView.as_view(), name='groups'),
    path('groups/add', views.AddStudentsView.as_view(), name='add_groups'),
    path('groups/delete', views.DeleteStudentsView.as_view(), name='remove_groups'),
    path('groups/update', views.UpdateGroupsView.as_view(), name='update_groups'),

    path('sessions/assign', views.AssignSessionsView.as_view(),
         name="assign_sessions"),
    path('timeslots/blocked', views.BlockTimeSlotsView.as_view(),
         name="blocked_timeslots"),
    path('sessions/consecutive', views.ConsecutiveSessionsView.as_view(),
         name="consecutive_sessions"),

    #################################################################################

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
    path('subject_statistics', views.subjectStatistics,
         name='subject_statistics'),
    path('student_statistics', views.studentStatistics, name='student_statistics'),
    path('statistics', views.statistics, name='statistics'),
    path('statistics/lecturerCount', views.lecturerCount, name='lecturerCount'),
    path('statistics/lecturerCenterStats',
         views.lecturerCenterStats, name='lecturerCenterStats'),
    path('statistics/lecurerLevelStat',
         views.lecurerLevelStat, name='lecurerLevelStat'),
    #     path('statistics/subjectCount', views.subjectCount, name='subjectCount'),
    path('statistics/allSubjectStatistics',
         views.allSubjectStatistics, name='allSubjectStatistics'),
    path('statistics/allProgrammeStatistics',
         views.allProgrammeStatistics, name='allProgrammeStatistics'),
    path('statistics/allYearSemesterStatistics',
         views.allYearSemesterStatistics, name='allYearSemesterStatistics'),
    path('statistics/allGroupStatistics',
         views.allGroupStatistics, name='allGroupStatistics'),
    path('statistics/allSubGroupStatistics',
         views.allSubGroupStatistics, name='allSubGroupStatistics'),

    # rooms
    path('rooms/lecturerRooms', views.lecturerRooms, name='lecturerRooms'),
    path('rooms/tagRooms', views.tagRooms, name='tagRooms'),
    path('rooms/loadLecturers', views.loadLecturers, name='loadLecturers'),
    path('rooms/loadRooms', views.loadRooms, name='loadRooms'),
    path('rooms/groupRooms', views.groupRooms, name='groupRooms'),
    path('rooms/sessionRooms', views.sessionRooms, name='sessionRooms'),
    path('rooms/consecutiveSessionRooms',
         views.consecutiveSessionRooms, name='consecutiveSessionRooms'),
    path('rooms/subjectRooms', views.subjectRooms, name='subjectRooms'),
    path('rooms/timeRooms', views.timeRooms, name='timeRooms'),
    path('rooms/addUnavailableRooms',
         views.addUnavailableRooms.as_view(), name='adddUnavailableRooms'),
    path('rooms/deleteAllUnavailableRooms',
         views.deleteAllUnavailableRooms, name='deleteAllUnavailableRooms'),
    path('rooms/deleteUnavailableRoom',
         views.deleteUnavailableRoom, name='deleteUnavailableRoom'),
    path('rooms/addLecturerRooms',
         views.addLecturerRooms.as_view(), name='addLecturerRooms'),
    path('rooms/deleteLecturerRooms',
         views.deleteLecturerRooms, name='deleteLecturerRooms'),
    path('rooms/deleteAllLecturerRooms',
         views.deleteAllLecturerRooms, name='deleteAllLecturerRooms'),
    path('rooms/loadGroups', views.loadGroups, name='loadGroups'),
    path('rooms/loadSubGroups', views.loadSubGroups, name='loadSubGroups'),
    path('rooms/loadTags', views.loadTags, name='loadTags'),
    path('rooms/addTagRoom', views.addTagRoom, name='addTagRoom'),
    path('rooms/deleteTagRoom', views.deleteTagRoom, name='deleteTagRoom'),
    path('rooms/deleteAllTagRooms',
         views.deleteAllTagRooms, name='deleteAllTagRooms'),
    path('rooms/addGroupRoom', views.addGroupRoom, name='addGroupRoom'),
    path('rooms/addSubGroupRoom', views.addSubGroupRoom, name='addSubGroupRoom'),
    path('rooms/deleteGroupRooms', views.deleteGroupRooms, name='deleteGroupRooms'),
    path('rooms/deleteSubGroupRooms',
         views.deleteSubGroupRooms, name='deleteSubGroupRooms'),
    path('rooms/deleteAllGroupRooms',
         views.deleteAllGroupRooms, name='deleteAllGroupRooms'),
    path('rooms/loadSubjects', views.loadSubjects, name='loadSubjects'),
    path('rooms/addSubjectTagRoom',
         views.addSubjectTagRoom, name='addSubjectTagRoom'),
    path('rooms/deleteSubjectTagRoom',
         views.deleteSubjectTagRoom, name='deleteSubjectTagRoom'),
    path('rooms/loadGroupSessions',
         views.loadGroupSessions, name='loadGroupSessions'),
    path('rooms/loadSubGroupSessions',
         views.loadSubGroupSessions, name='loadSubGroupSessions'),
    path('rooms/addSessionRooms', views.addSessionRooms, name='addSessionRooms'),
    path('rooms/deleteSessionRooms',
         views.deleteSessionRooms, name='deleteSessionRooms'),
    path('rooms/deleteAllSubjectTagRooms',
         views.deleteAllSubjectTagRooms, name='deleteAllSubjectTagRooms'),
    path('rooms/deleteAllSessionRooms',
         views.deleteAllSessionRooms, name='deleteAllSessionRooms'),

    # ranul
    #################################################################################
]
