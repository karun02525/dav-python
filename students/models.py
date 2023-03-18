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
        return self.class_name


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

    DOC_TYPE = (
        ('pan', 'PAN Card'),
        ('aadhar', 'Aadhar Card'),
        ('Passport', 'Passport'),
        ('dl', 'Driving License'),
        ('voter_id', 'Voter ID'),
    )

    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=10, blank=True)
    mobile = models.CharField(max_length=10, unique=True, blank=True,
                              validators=[RegexValidator('^[0-9]{10}$', 'Invalid mobile no')], )
    email = models.EmailField(max_length=30, unique=True, blank=True)
    dob = models.DateField(blank=True, default='2023-03-17')
    gender = models.CharField(max_length=6, choices=GENDER, blank=True)
    blood_group = models.CharField(max_length=6, blank=True)
    address = models.TextField(validators=[MaxLengthValidator(50)], blank=True)
    state = models.CharField(max_length=10, blank=True)
    dist = models.CharField(max_length=10, blank=True)
    pincode = models.CharField(max_length=6, blank=True,
                               validators=[RegexValidator('^[0-9]{6}$', 'Invalid postal code')])
    parent_mobile = models.CharField(max_length=10, blank=True,
                                     validators=[RegexValidator('^[0-9]{10}$', 'Invalid mobile no')])
    parent_email = models.EmailField(max_length=30, blank=True)
    father_name = models.CharField(max_length=30, blank=True)
    mother_name = models.CharField(max_length=30, blank=True)
    father_occupation = models.CharField(max_length=30, blank=True)
    mother_occupation = models.CharField(max_length=30, blank=True)
    parent_doc_type = models.CharField(max_length=10, choices=DOC_TYPE, blank=True)
    parent_doc_no = models.CharField(max_length=10, blank=True)
    student_doc_type = models.CharField(max_length=15, choices=DOC_TYPE, blank=True)
    student_doc_no = models.CharField(max_length=15, blank=True)
    student_pic = models.ImageField(upload_to=get_file_path, blank=True, null=True,
                                    validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jgg'])])
    parent_pic = models.ImageField(upload_to=get_file_path, blank=True, null=True,
                                   validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])])
    student_doc_pdf = models.FileField(upload_to=get_file_path, blank=True, null=True,
                                       validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])
    parent_doc_pdf = models.FileField(upload_to=get_file_path, blank=True, null=True,
                                      validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])

    def __str__(self):
        return self.first_name + " " + self.last_name
