from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet as DjoserUserViewSet

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

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


class FilterOptionsViewSet(viewsets.ViewSet):
    def list(self, request):
        model_serializers = {
            Position: PositionSerializer,
            Grade: GradeSerializer,
            AcademicStatus: AcademicStatusSerializer,
            WorkExperience: WorkExperienceSerializer,
            Location: LocationSerializer,
            EmploymentStatus: EmploymentStatusSerializer,
        }

        data = {}

        for model, serializer in model_serializers.items():
            queryset = model.objects.all()
            data[model.__name__] = serializer(queryset, many=True).data

        data["has_higher_education"] = False
        data["has_participated_in_hackathons"] = False
        data["has_personal_projects"] = False
        data["skills_verified"] = False
        data["has_video_presentation"] = False

        return Response(data)
