from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import serializers
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_student': 'all/',
        'specific_student': 'find/?parm=value',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/student/pk/delete'
    }
    return Response(api_urls)


@api_view(['GET'])
def view_students(request):
    students = Student.objects.all()
    if students:
        data = StudentSerializer(students, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_student(request):
    if request.query_params:
        students = Student.objects.filter(**request.query_params.dict())
        if len(students) != 0:
            data = StudentSerializer(students, many=True)
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_student(request):
    student = StudentSerializer(data=request.data)
    if Student.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if student.is_valid():
        student.save()
        return Response(student.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_student(request, pk):
    student_id = Student.objects.get(pk=pk)
    data = StudentSerializer(instance=student_id, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
