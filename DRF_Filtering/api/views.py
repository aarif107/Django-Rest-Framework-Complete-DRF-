from django.shortcuts import render
from .models import Student
from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer


class StudentList(ListAPIView):
    queryset=Student.objects.filter(passby='maximilian')
    serializer_class=StudentSerializer
    def get_queryset(self):
        user=self.request.user
        return Student.objects.filter(passby=user)
