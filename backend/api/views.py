from rest_framework import viewsets

from students.models import StudentResume

from .serializers import StudentUserSerializer


class StudentUserViewSet(viewsets.ModelViewSet):
    queryset = StudentResume.objects.all()
    serializer_class = StudentUserSerializer
