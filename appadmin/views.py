from django.db import IntegrityError
from rest_framework import viewsets
from .models import AssignRollNoModel
from .serializers import AssignRollNoSerializer
from rest_framework.response import Response
from rest_framework import status
from students.models import Student, Classes
from students.serializers import StudentsSerializer, ClassesSerializer


# Create your views here.
class AssignRollNoViewSet(viewsets.ModelViewSet):
    serializer_class = AssignRollNoSerializer
    queryset = AssignRollNoModel

    def list(self, request, *args, **kwargs):
        model = AssignRollNoModel.objects.all()
        serializer = AssignRollNoSerializer(model, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = AssignRollNoModel.objects.filter(roll_no=pk)
        serializer = AssignRollNoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            update_data = AssignRollNoModel.objects.create(
                roll_no=data['roll_no'],
                is_active=data['is_active'],
                classes_id=data['class_id'],
                student_id=data['student_id'])
            update_data.save()
            data = {'mess': f"successfully update roll no {data['roll_no']}", 'status': True}
            return Response(data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # for i in data['classes']:
