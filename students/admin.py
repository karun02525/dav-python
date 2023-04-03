from django.contrib import admin
from .models import Classes, Student


class AdminStudent(admin.ModelAdmin):
    list_display = ['classes', 'roll_no', 'first_name', 'last_name', 'mobile', 'gender', 'father_name', 'parent_email',
                    'student_id']


class AdminClasses(admin.ModelAdmin):
    list_display = ['class_name', 'class_id']


admin.site.register(Student, AdminStudent)
admin.site.register(Classes, AdminClasses)
