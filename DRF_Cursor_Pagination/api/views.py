from django.shortcuts import render
from .models import Student
from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer
from .paginations import MyCursorPagination


class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=MyCursorPagination
