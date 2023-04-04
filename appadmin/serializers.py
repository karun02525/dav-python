import uuid

from rest_framework import serializers
from students.serializers import StudentsSerializer, ClassesSerializer
from students.models import Classes, Student
from django.forms.models import model_to_dict


# model_to_dict(obj)


class AssignRollNoSerializer(serializers.ModelSerializer):
    roll_no = serializers.IntegerField(default=0)

    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, data):
        if data['roll_no'] == '':
            raise serializers.ValidationError({"message": 'Please enter roll no'})
        return data

    #  exclude = ('roll_no', 'class_id', 'class_name', 'stud_id', 'first_name')
    # fields = ('roll_no', 'class_id', 'class_name', 'stud_id', 'first_name')
