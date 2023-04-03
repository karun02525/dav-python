import uuid

from django.db import models


class BaseModel(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class AssignRollNoModel(BaseModel):
    assign_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class_id = models.UUIDField(max_length=40)
    student_id = models.UUIDField(max_length=40)
    full_name = models.CharField(max_length=40)
    class_name = models.CharField(max_length=10)
    roll_no = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)




