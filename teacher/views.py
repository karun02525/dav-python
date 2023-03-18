import os

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

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


class TeacherFileUploadAV(APIView):
    serializer_class = TeacherSerializer
    queryset = Teacher

    def patch(self, request):
        teacher_id = self.request.query_params.get('teacher_id', None)
        type = self.request.query_params.get('type', None)
        model = Teacher.objects.get(pk=teacher_id)
        serializer = TeacherSerializer(model, data=request.data)

        if serializer.is_valid():
            if type == 'teacher_pic':
                return teacher_update_pic(request, model)
            elif type == 'teacher_doc_pdf':
                return teacher_update_doc(request, model)
            else:
                return Response({"message": 'enter invalid type'}, status=HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        teacher_id = self.request.query_params.get('teacher_id', None)
        type = self.request.query_params.get('type', None)
        model = Teacher.objects.get(pk=teacher_id)

        try:
            if type == 'teacher_pic':
                try:
                    os.remove(model.teacher_pic.path)
                    model.teacher_pic = ""
                    model.save()
                except Exception as e:
                    model.teacher_pic = ""
                    model.save()
                    print(e)
            elif type == 'teacher_doc_pdf':
                try:
                    os.remove(model.teacher_doc_pdf.path)
                    model.teacher_doc_pdf = ""
                    model.save()
                except Exception as e:
                    model.teacher_doc_pdf = ""
                    model.save()
                    print(e)
            else:
                return Response({"message": "enter invalid user id or type value"}, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'msg': 'delete successfully'})


''''************ STUDENT UPLOAD PROFILE PIC ****************'''


def teacher_update_pic(request, model):
    try:
        if len(request.FILES) != 0:
            if model.teacher_pic.name != '':
                try:
                    os.remove(model.teacher_pic.path)
                    saveTeacherPic(model, request)
                except FileNotFoundError as e:
                    saveTeacherPic(model, request)
            else:
                saveTeacherPic(model, request)

        return Response({'msg': 'update successfully', 'data': str(model.teacher_pic)})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


''''************  UPLOAD TEACHER DOCUMENTS ****************'''


def teacher_update_doc(request, model):
    try:
        if len(request.FILES) != 0:
            if model.teacher_doc_pdf.name is None or model.teacher_doc_pdf.name != '':
                try:
                    os.remove(model.teacher_doc_pdf.path)
                    saveTeacherDocPdf(request, model)
                except FileNotFoundError as e:
                    saveTeacherDocPdf(request, model)
                    print(e)
            else:
                saveTeacherDocPdf(request, model)

        return Response({'msg': 'update successfully', 'data': str(model.teacher_doc_pdf)})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


def saveTeacherPic(model, request):
    model.teacher_pic = request.FILES['teacher_pic']
    model.save()


def saveTeacherDocPdf(request, model):
    model.teacher_doc_pdf = request.FILES['teacher_doc_pdf']
    model.save()
