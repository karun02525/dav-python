from rest_framework import serializers
from .models import AssignRollNoModel
from students.serializers import StudentsSerializer, ClassesSerializer
from students.models import Classes, Student
from django.forms.models import model_to_dict


# model_to_dict(obj)


class AssignRollNoSerializer(serializers.ModelSerializer):
    student = StudentsSerializer(many=False, read_only=True)
    classes = ClassesSerializer(many=False, read_only=True)

    class Meta:
        model = AssignRollNoModel
        fields = '__all__'
    #  exclude = ('roll_no', 'class_id', 'class_name', 'stud_id', 'first_name')
    # fields = ('roll_no', 'class_id', 'class_name', 'stud_id', 'first_name')
