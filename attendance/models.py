import uuid

from django.db import models
from teacher.models import Teacher


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class StudentAttendanceModel(BaseModel):
    ATTENDANCE = (
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('holiday', 'Holiday'),
        ('holiday', 'Holiday'),
        ('leave', 'Leave'),
        ('vacation', 'Vacation'),
        ('half_day_leave', 'Half-Day Leave'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teacher_id = models.CharField(max_length=40)
    teacher_name = models.CharField(max_length=40)
    class_id = models.CharField(max_length=40)
    class_name = models.CharField(max_length=40)
    student_id = models.CharField(max_length=40,)
    student_name = models.CharField(max_length=40,)
    status = models.CharField(max_length=20, choices=ATTENDANCE)
    message = models.CharField(max_length=100, blank=True, )

    class Meta:
        db_table = "attendance"
