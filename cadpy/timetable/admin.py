from django.contrib import admin

# Register your models here.
from .models import Lecturer, Group, Subgroup, Tags, Session, ParallelSession
from .models import Subjects

admin.site.register(Lecturer)
admin.site.register(Subjects)
admin.site.register(Session)
admin.site.register(ParallelSession)

