from django.contrib.admin import ModelAdmin, register
from .models import StudentAttendanceModel


@register(StudentAttendanceModel)
class AttendanceAdmin(ModelAdmin):
    list_display = (
        'teacher_name', 'class_name', 'student_name', 'status', 'message', 'created_at')


