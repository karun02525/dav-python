from rest_framework import viewsets
from rest_framework.response import Response

from .models import Teacher
from .serializers import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher

    def list(self, request, *args, **kwargs):
        queryset = Teacher.objects.all()
        serializer = TeacherSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Teacher.objects.filter(teacher_id=pk)
        serializer = TeacherSerializer(queryset, many=True)
        return Response(serializer.data)
