from rest_framework import serializers
from .models import StudentAttendanceModel


class StudentAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendanceModel
        fields = '__all__'
