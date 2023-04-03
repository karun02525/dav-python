import json

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StudentAttendanceModel
from .serializers import StudentAttendanceSerializer
from rest_framework import status


class StudentAttendance(APIView):

    def get(self, request, pk=None):
        if pk is not None:
            queryset = StudentAttendanceModel.objects.filter(student_id=pk)
            serializer = StudentAttendanceSerializer(queryset, many=True)
            return Response({'status': True, 'message': 'success','data': serializer.data})
        return Response({'message': 'please enter valid student id', 'status': False, },
                        status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        data = request.data
        teacher_id = data['teacher_id']
        class_id = data['class_id']
        if StudentAttendanceModel.objects.filter(teacher_id=teacher_id, class_id=class_id):
            return Response({'status': True, 'msg': 'Attendance already submitted'})
        else:
            return attendance_operation(teacher_id, class_id, data)
        # serializer = StudentAttendanceSerializer(data=saveData)


def attendance_operation(teacher_id, class_id, data):
    attendances = data['attendances']
    teacher_name = data['teacher_name']
    class_name = data['class_name']

    saveData = {'teacher_id': teacher_id,
                'teacher_name': teacher_name,
                'class_id': class_id,
                'class_name': class_name}
    for attend in attendances:
        student_id = attend['student_id']
        student_name = attend['student_name']
        status = attend['status']
        message = attend['message']

        saveData['student_id'] = student_id
        saveData['student_name'] = student_name
        saveData['status'] = status
        saveData['message'] = message
        serializer = StudentAttendanceSerializer(data=saveData)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    return Response({'status': True, 'msg': 'Attendance submitted successfully'})
