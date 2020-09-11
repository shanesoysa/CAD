from django.contrib import admin

# Register your models here.
from .models import Lecturer
from .models import Subjects

admin.site.register(Lecturer)
admin.site.register(Subjects)

