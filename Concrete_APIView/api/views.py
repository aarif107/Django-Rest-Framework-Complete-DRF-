from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


class LC_StudnetAPI(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class RUD_StudentAPI(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


