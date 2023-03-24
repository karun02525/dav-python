# Generated by Django 4.1.7 on 2023-03-24 20:50

import django.core.validators
from django.db import migrations, models
import teacher.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('teacher_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=10)),
                ('last_name', models.CharField(blank=True, max_length=10)),
                ('mobile', models.CharField(blank=True, max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{10}$', 'Invalid mobile no')])),
                ('email', models.EmailField(blank=True, max_length=30, unique=True)),
                ('dob', models.DateField(blank=True, default='2023-03-17')),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=6)),
                ('address', models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(50)])),
                ('state', models.CharField(blank=True, max_length=10)),
                ('dist', models.CharField(blank=True, max_length=10)),
                ('pincode', models.CharField(blank=True, max_length=6, validators=[django.core.validators.RegexValidator('^[0-9]{6}$', 'Invalid postal code')])),
                ('parent_mobile', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]{10}$', 'Invalid mobile no')])),
                ('parent_name', models.CharField(blank=True, max_length=30)),
                ('teacher_occupation', models.CharField(blank=True, max_length=30)),
                ('teacher_qualification', models.CharField(blank=True, max_length=30)),
                ('teacher_doc_type', models.CharField(blank=True, choices=[('pan', 'PAN Card'), ('aadhar', 'Aadhar Card'), ('Passport', 'Passport'), ('dl', 'Driving License'), ('voter_id', 'Voter ID')], max_length=15)),
                ('teacher_doc_no', models.CharField(blank=True, max_length=15)),
                ('teacher_pic', models.ImageField(blank=True, null=True, upload_to=teacher.models.get_file_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])])),
                ('teacher_doc_pdf', models.FileField(blank=True, null=True, upload_to=teacher.models.get_file_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
