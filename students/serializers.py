from rest_framework import serializers
from .models import Classes, Student


class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    # def validate(self, data):
    #     blood_group = data.get('blood_group')
    #     if not blood_group == "+A":
    #         raise serializers.ValidationError({"msg": 'please enter valid blood grop'})
    #     return data
    #
    # def validate(self, data):
    #     blood_group = data.get('blood_group')
    #     if not blood_group == "+A":
    #         raise serializers.ValidationError({"msg": 'please enter valid blood grop'})
    #     return data
