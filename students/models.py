from django.core.validators import RegexValidator, MaxLengthValidator, FileExtensionValidator
from django.db import models
import uuid
from rest_framework import serializers
import os


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Classes(BaseModel):
    class_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class_name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.class_name + "=> " + str(self.class_id)


def address_validation(value):
    if len(value) == 30:
        return value
    else:
        raise serializers.ValidationError("enter full address not more than 30")


def get_file_path(instance, filename):
    #  prefix = instance.student_pic.file.field_name
    # mobile = getattr(instance, 'mobile', None)
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('documents/', filename)


class Student(BaseModel):

    def image_file_path(self, filename):
        return '/'.join(['images', str(self.first_name), filename])

    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    STATE = (
        ('bihar', 'Bihar'),
        ('up', 'UP'),
        ('jh', 'Jharkhand'),
    )

    DOC_TYPE = (
        ('pan', 'PAN Card'),
        ('aadhar', 'Aadhar Card'),
        ('Passport', 'Passport'),
        ('dl', 'Driving License'),
        ('voter_id', 'Voter ID'),
    )

    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    roll_no = models.PositiveIntegerField(default=0)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE, related_name="classes", default=None, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10, unique=True,
                              validators=[RegexValidator('^[0-9]{10}$', 'Invalid mobile no')], )
    email = models.EmailField(max_length=30, unique=True)
    dob = models.DateField(default='2023-03-17')
    gender = models.CharField(max_length=6, choices=GENDER)
    blood_group = models.CharField(max_length=6, )
    address = models.TextField(validators=[MaxLengthValidator(50)], )
    state = models.CharField(max_length=10, choices=STATE)
    dist = models.CharField(max_length=10)
    pincode = models.CharField(max_length=6,
                               validators=[RegexValidator('^[0-9]{6}$', 'Invalid postal code')])
    parent_mobile = models.CharField(max_length=10,
                                     validators=[RegexValidator('^[0-9]{10}$', 'Invalid mobile no')])
    parent_email = models.EmailField(max_length=30)
    father_name = models.CharField(max_length=30, )
    mother_name = models.CharField(max_length=30, )
    father_occupation = models.CharField(max_length=30, )
    mother_occupation = models.CharField(max_length=30, )
    parent_doc_type = models.CharField(max_length=10, choices=DOC_TYPE, )
    parent_doc_no = models.CharField(max_length=10, )
    student_doc_type = models.CharField(max_length=15, choices=DOC_TYPE, )
    student_doc_no = models.CharField(max_length=15, )
    student_pic = models.ImageField(upload_to=get_file_path, blank=True, null=True,
                                    validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])])
    parent_pic = models.ImageField(upload_to=get_file_path, blank=True, null=True,
                                   validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])])
    student_doc_pdf = models.FileField(upload_to=get_file_path, blank=True, null=True,
                                       validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])
    parent_doc_pdf = models.FileField(upload_to=get_file_path, blank=True, null=True,
                                      validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])

    def __str__(self):
        return self.first_name + " " + self.last_name
