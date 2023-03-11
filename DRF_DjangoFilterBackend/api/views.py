from django.shortcuts import render
from .models import Student
from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend


class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['name','city']
