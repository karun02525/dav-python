from .serializers import AssignRollNoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from students.models import Student
from django.db.models import Q


class AssignRollNoView(APIView):
    serializer_class = AssignRollNoSerializer

    def patch(self, request, student_id: None):
        # student_id = self.request.query_params.get('student_id', '')
        try:
            queryset = Student.objects.get(student_id=student_id)

            if Student.objects.filter(
                    Q(classes=queryset.classes.class_id) & Q(roll_no=request.data['roll_no'])).exists():
                return Response({'status': False, 'message': 'roll no already exists'}, status=status.HTTP_200_OK)

            serializer = AssignRollNoSerializer(queryset, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'message': 'roll no update success'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
