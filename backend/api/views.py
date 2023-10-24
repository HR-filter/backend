from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet as DjoserUserViewSet

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from students.models import (
    AcademicStatus,
    EmploymentStatus,
    Grade,
    Location,
    Position,
    StudentResume,
    User,
    WorkExperience,
)

from .filters import StudentResumeFilter
from .serializers import (
    AcademicStatusSerializer,
    EmploymentStatusSerializer,
    GradeSerializer,
    LocationSerializer,
    PositionSerializer,
    StudentUserSerializer,
    UserSerializer,
    WorkExperienceSerializer,
)


class StudentUserViewSet(viewsets.ModelViewSet):
    queryset = StudentResume.objects.all()
    serializer_class = StudentUserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StudentResumeFilter


class PublicUserViewSet(DjoserUserViewSet):
    """Представление для работы с публичными данными пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    # permission_classes = [IsAuthenticated]


class StudentResumeViewSet(viewsets.ModelViewSet):
    queryset = StudentResume.objects.all()
    serializer_class = StudentUserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StudentResumeFilter


class FilterOptionsView(APIView):
    def get(self, request):
        # Получить данные для каждой модели
        positions = Position.objects.all()
        grades = Grade.objects.all()
        academic_statuses = AcademicStatus.objects.all()
        work_experiences = WorkExperience.objects.all()
        locations = Location.objects.all()
        employment_statuses = EmploymentStatus.objects.all()

        # Сериализовать данные
        data = {
            "Position": PositionSerializer(positions, many=True).data,
            "Grade": GradeSerializer(grades, many=True).data,
            "AcademicStatus": AcademicStatusSerializer(
                academic_statuses, many=True
            ).data,
            "WorkExperience": WorkExperienceSerializer(
                work_experiences, many=True
            ).data,
            "Location": LocationSerializer(locations, many=True).data,
            "EmploymentStatus": EmploymentStatusSerializer(
                employment_statuses, many=True
            ).data,
        }

        return Response(data)
