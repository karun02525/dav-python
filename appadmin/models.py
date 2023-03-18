import uuid

from django.db import models
from students.models import Classes, Student


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class AssignRollNoModel(models.Model):
    assign_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, related_name='classes', null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student', null=True)
    roll_no = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"Roll No.  {self.roll_no} :   {self.classes.class_name}  :  {self.student.first_name} {self.student.last_name} "
