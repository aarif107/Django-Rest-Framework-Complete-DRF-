from django.shortcuts import render
from .models import Student
from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer
from .paginations import MyPageNumberPagination


class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=MyPageNumberPagination
