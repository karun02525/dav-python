import uuid
import os
from django.core.validators import MaxLengthValidator, RegexValidator, FileExtensionValidator
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('documents/', filename)


class Teacher(BaseModel):
    STATE = (
        ('bihar', 'Bihar'),
        ('up', 'UP'),
        ('jh', 'Jharkhand'),
    )

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

    teacher_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10,)
    mobile = models.CharField(max_length=10, unique=True,
                              validators=[RegexValidator('^[0-9]{10}$', 'Invalid mobile no')], )
    email = models.EmailField(max_length=30, unique=True, )
    dob = models.DateField(blank=True, default='2023-03-17')
    gender = models.CharField(max_length=6, choices=GENDER, )
    address = models.TextField(validators=[MaxLengthValidator(50)], )
    state = models.CharField(max_length=10, choices=STATE)
    dist = models.CharField(max_length=10,)
    pincode = models.CharField(max_length=6,
                               validators=[RegexValidator('^[0-9]{6}$', 'Invalid postal code')])
    parent_mobile = models.CharField(max_length=10,
                                     validators=[RegexValidator('^[0-9]{10}$', 'Invalid mobile no')])
    parent_name = models.CharField(max_length=30)
    teacher_occupation = models.CharField(max_length=30)
    teacher_qualification = models.CharField(max_length=30)
    teacher_doc_type = models.CharField(max_length=15, choices=DOC_TYPE)
    teacher_doc_no = models.CharField(max_length=15, )
    teacher_pic = models.ImageField(upload_to=get_file_path, blank=True, null=True,
                                    validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])])

    teacher_doc_pdf = models.FileField(upload_to=get_file_path, blank=True, null=True,
                                       validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])

    def __str__(self):
        return self.first_name + " " + self.last_name


