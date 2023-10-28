from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

from djoser.views import UserViewSet as DjoserUserViewSet

from drf_yasg.utils import swagger_auto_schema

from rest_framework import filters, viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from students.models import (
    AcademicStatus,
    EmploymentStatus,
    Grade,
    Location,
    StudentResume,
    User,
    Experience,
    FavoriteResume,
)

from .filters import StudentResumeFilter
from .serializers import (
    AcademicStatusSerializer,
    EmploymentStatusSerializer,
    GradeSerializer,
    LocationSerializer,
    UserSerializer,
    ExperienceSerializer,
    StudentResumeSerializer,
    FavoriteSerializer,
)


class StudentUserViewSet(viewsets.ModelViewSet):
    queryset = StudentResume.objects.all()
    serializer_class = StudentResumeSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = StudentResumeFilter

    @action(
        detail=True,
        methods=["post"],
    )
    def favorite(self, request, pk):
        resume = get_object_or_404(StudentResume, id=pk)
        user = request.user
        data = {"user": user.id, "recipe": resume.id}

        serializer = FavoriteSerializer(
            data=data,
            context={"request": request},
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @favorite.mapping.delete
    def delete_favorite(self, request, pk):
        recipe = get_object_or_404(StudentResume, id=pk)
        user = request.user
        favorite = get_object_or_404(
            FavoriteResume,
            user=user,
            recipe=recipe,
        )

        favorite.delete()
        message = {"message": "Резюме успешно удалён из избранного."}
        return Response(message, status=status.HTTP_204_NO_CONTENT)


class PublicUserViewSet(DjoserUserViewSet):
    """Представление для работы с публичными данными пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    # permission_classes = [IsAuthenticated]


class FilterOptionsViewSet(viewsets.ViewSet):
    @swagger_auto_schema(operation_id="list_filters")
    def list(self, request):
        model_serializers = {
            Grade: GradeSerializer,
            AcademicStatus: AcademicStatusSerializer,
            Experience: ExperienceSerializer,
            Location: LocationSerializer,
            EmploymentStatus: EmploymentStatusSerializer,
        }

        data = {}

        for model, serializer in model_serializers.items():
            queryset = model.objects.all()
            data[model.__name__] = serializer(queryset, many=True).data

        return Response(data)


class FilterBooleanOpitionViewSet(viewsets.ViewSet):
    @swagger_auto_schema(operation_id="list_boolean-filters")
    def list(self, request):
        default_options = [
            "has_higher_education",
            "has_participated_in_hackathons",
            "has_personal_projects",
            "skills_verified",
            "has_video_presentation",
        ]

        data = {option: False for option in default_options}

        return Response(data)
