from django.contrib import admin
from .models import Teacher


class AdminTeacher(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'mobile', 'email', 'gender', 'parent_name', ]


admin.site.register(Teacher, AdminTeacher)
