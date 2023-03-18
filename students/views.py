from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST
from .serializers import ClassesSerializer, StudentsSerializer
from .models import Classes, Student
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
import os


# Create your views here.
# queryset = TodoModel.objects.all().order_by('id')

class ClassesViewSet(viewsets.ModelViewSet):
    serializer_class = ClassesSerializer
    queryset = Classes

    def list(self, request, *args, **kwargs):
        queryset = Classes.objects.all()
        serializer = ClassesSerializer(queryset, many=True)

        if not serializer.data:
            msg = 'class data empty!'
        else:
            msg = 'successfully get classes list'

        data = {
            'mess': msg,
            'data': serializer.data,
            'status': True
        }
        return Response(data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Classes.objects.filter(class_name=pk)
        serializer = ClassesSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def update_class(self, request):
        cid = self.request.query_params.get('class_id')
        queryset = Classes.objects.filter(class_id=cid)
        serializer = ClassesSerializer(queryset, many=True)
        return Response(serializer.data)


class StudentsViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentsSerializer
    queryset = Student

    def list(self, request, *args, **kwargs):
        queryset = Student.objects.all()
        serializer = StudentsSerializer(queryset, many=True)
        print('*************************',request.user)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print('*************************', request.user)
        queryset = Student.objects.filter(stud_id=pk)
        serializer = StudentsSerializer(queryset, many=True)
        return Response(serializer.data)


class StudentFileUploadAV(APIView):
    serializer_class = StudentsSerializer
    queryset = Student

    def patch(self, request):
        # pk = self.kwargs.get('pk')
        # if pk is None:
        #     return Response({"message": "Invalid request"}, status=HTTP_400_BAD_REQUEST)
        student_id = self.request.query_params.get('student_id', None)
        type = self.request.query_params.get('type', None)
        model = Student.objects.get(pk=student_id)
        serializer = StudentsSerializer(model, data=request.data)

        if serializer.is_valid():
            if type == 'student_pic':
                return upload_student_pic(request, model)
            elif type == 'parent_pic':
                return upload_parent_pic(request, model)
            elif type == 'student_doc_pdf':
                return upload_student_doc(request, model)
            elif type == 'parent_doc_pdf':
                return upload_parent_doc(request, model)
            else:
                return Response({"message": 'enter invalid type'}, status=HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        student_id = self.request.query_params.get('student_id', None)
        type = self.request.query_params.get('type', None)
        model = Student.objects.get(pk=student_id)

        try:
            if type == 'student_pic':
                try:
                    os.remove(model.student_pic.path)
                    model.student_pic = ""
                    model.save()
                except Exception as e:
                    model.student_pic = ""
                    model.save()
                    print(e)

            elif type == 'parent_pic':
                try:
                    os.remove(model.parent_pic.path)
                    model.parent_pic = ""
                    model.save()
                except Exception as e:
                    model.parent_pic = ""
                    model.save()
                    print(e)
            elif type == 'student_doc_pdf':
                try:
                    os.remove(model.student_doc_pdf.path)
                    model.student_doc_pdf = ""
                    model.save()
                except Exception as e:
                    model.student_doc_pdf = ""
                    model.save()
                    print(e)

            elif type == 'parent_doc_pdf':
                try:
                    os.remove(model.parent_doc_pdf.path)
                    model.parent_doc_pdf = ""
                    model.save()
                except Exception as e:
                    model.parent_doc_pdf = ""
                    model.save()
                    print(e)
            else:
                return Response({"message": "enter invalid user id or type value"}, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'msg': 'delete successfully'})


''''************ STUDENT UPLOAD PROFILE PIC ****************'''


def upload_student_pic(request, model):
    try:
        if len(request.FILES) != 0:
            if model.student_pic.name != '':
                try:
                    os.remove(model.student_pic.path)
                    saveStudentPic(model, request)
                except FileNotFoundError as e:
                    saveStudentPic(model, request)
            else:
                saveStudentPic(model, request)

        return Response({'msg': 'update successfully', 'data': str(model.student_pic)})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


''''************ PARENT UPLOAD PROFILE ****************'''


def upload_parent_pic(request, model):
    try:
        if len(request.FILES) != 0:
            if model.parent_pic.name != '':
                try:
                    os.remove(model.parent_pic.path)
                    saveParentPic(model, request)
                except FileNotFoundError as e:
                    saveParentPic(model, request)
                    print(e)
            else:
                saveParentPic(model, request)

        return Response({'msg': 'update successfully', 'data': str(model.parent_pic)})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


''''************  UPLOAD STUDENT DOCUMENTS ****************'''


def upload_student_doc(request, model):
    try:
        if len(request.FILES) != 0:
            if model.student_doc_pdf.name is None or model.student_doc_pdf.name != '':
                try:
                    os.remove(model.student_doc_pdf.path)
                    saveStudentDocPdf(model, request)
                except FileNotFoundError as e:
                    saveStudentDocPdf(model, request)
                    print(e)
            else:
                saveStudentDocPdf(model, request)

        return Response({'msg': 'update successfully', 'data': str(model.student_doc_pdf)})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


''''************ UPLOAD PARENT DOCMENTS ****************'''


def upload_parent_doc(request, model):
    try:
        if len(request.FILES) != 0:
            if model.parent_doc_pdf.name is None or model.parent_doc_pdf.name != '':
                try:
                    os.remove(model.parent_doc_pdf.path)
                    saveParentDocPdf(model, request)
                except FileNotFoundError as e:
                    saveParentDocPdf(model, request)
                    print(e)
            else:
                saveParentDocPdf(model, request)

        return Response({'msg': 'update successfully', 'data': str(model.parent_doc_pdf)})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


def saveStudentPic(model, request):
    model.student_pic = request.FILES['student_pic']
    model.save()


def saveParentPic(model, request):
    model.parent_pic = request.FILES['parent_pic']
    model.save()


def saveStudentDocPdf(model, request):
    model.student_doc_pdf = request.FILES['student_doc_pdf']
    model.save()


def saveParentDocPdf(model, request):
    model.parent_doc_pdf = request.FILES['parent_doc_pdf']
    model.save()

# def get_queryset(self):
#     # cid = self.request.query_params.get('id')
#     #   queryset = Classes.objects.filter(class_id=cid)
#     return Classes.objects.all()

# @action(detail=True, methods=["GET"], url_name="classes")
# def classes(self, request, id=None):
#     # class_id = self.get_object()
#     print("***********")
#     queryset = Classes.objects.filter(class_id=class_id)
#     serializer = ClassesSerializer(queryset, many=True)
#     return Response(serializer.data, status=200)
