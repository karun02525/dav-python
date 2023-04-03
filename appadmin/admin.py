from django.contrib import admin
from .models import AssignRollNoModel


class AssignRollNoStudent(admin.ModelAdmin):
    list_display = ['class_name', 'roll_no', 'full_name', 'is_verified', 'student_id', ]


admin.site.register(AssignRollNoModel, AssignRollNoStudent)
