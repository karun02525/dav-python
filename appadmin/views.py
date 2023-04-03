from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework import viewsets
from .models import AssignRollNoModel
from .serializers import AssignRollNoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from students.models import Student, Classes
from students.serializers import StudentsSerializer, ClassesSerializer


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

        try:
            serializer = AssignRollNoSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                data = {'mess': f"create roll no successfully update", 'status': True}
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except IntegrityError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UpdateRollNoView(APIView):

    def patch(self, request):
        student_id = self.request.query_params.get('student_id', '')
        try:
            obj = AssignRollNoModel.objects.get(student_id=student_id)
            serializer = AssignRollNoSerializer(obj, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                data = {'mess': f"Successfully Update Roll No", 'status': True}
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            # data = request.data
            # try:
            #     obj = Task.objects.filter(id=tasks['id']).first()
            #     serializer = self.serializer_class(obj, data={'status': 1}, partial=True)
            #     if serializer.is_valid():
            #         serializer.save()
            #
            #     update_data = AssignRollNoModel.objects.create(
            #         roll_no=data['roll_no'],
            #         is_active=data['is_active'],
            #         classes_id=data['class_id'],
            #         student_id=data['student_id'])
            #     update_data.save()

    # for i in data['classes']:
