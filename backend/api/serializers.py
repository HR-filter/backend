from djoser.serializers import UserCreateSerializer

from drf_extra_fields.fields import Base64ImageField

from rest_framework import serializers

from students.models import (
    AcademicStatus,
    ContactInfo,
    EmploymentStatus,
    Grade,
    Location,
    Skill,
    StudentResume,
    User,
    WorkExperience,
)


class UserSerializer(UserCreateSerializer):
    """Сериализатор для модели пользователя."""

    class Meta:
        model = User
        fields = [
            "email",
            "id",
            "username",
            "first_name",
            "last_name",
            "password",
        ]

        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        """Создаёт нового пользователя с запрошенными полями.

        Args:
            validated_data (dict): Полученные проверенные данные.

        Returns:
            User: Созданный пользователь.
        """
        user = User(
            email=validated_data["email"],
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()

        return user

    def to_representation(self, instance):
        """
        Преобразует объект пользователя в представление JSON.
        """
        data = super().to_representation(instance)
        request = self.context.get("request")

        if request.method == "GET":
            data.pop("password", None)

        return data


class ContactInfoSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели ContactInfo, предоставляет информацию
    о контактных данных.
    """

    class Meta:
        model = ContactInfo
        fields = [
            "phone_number",
            "alternate_email",
            "telegram_login",
        ]


class BaseExperienceSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": str(instance),
        }


class SkillSerializer(BaseExperienceSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name"]


class AcademicStatusSerializer(BaseExperienceSerializer):
    class Meta:
        model = AcademicStatus
        fields = ["id", "name"]


class GradeSerializer(BaseExperienceSerializer):
    class Meta:
        model = Grade
        fields = ["id", "name"]


class WorkExperienceSerializer(BaseExperienceSerializer):
    class Meta:
        model = WorkExperience
        fields = ["id", "name"]


class LocationSerializer(BaseExperienceSerializer):
    class Meta:
        model = Location
        fields = ["id", "name"]


class EmploymentStatusSerializer(BaseExperienceSerializer):
    class Meta:
        model = EmploymentStatus
        fields = ["id", "name"]


class StudentUserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="user.id")
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    contact_info = ContactInfoSerializer()
    photo = Base64ImageField()
    academic_status = AcademicStatusSerializer()
    employment_status = EmploymentStatusSerializer()
    skills = SkillSerializer(many=True)
    grade = GradeSerializer()
    work_experience = WorkExperienceSerializer()
    location = LocationSerializer()
    percentage_match = serializers.IntegerField(read_only=True, default=0)
    achievement = serializers.CharField()
    portfolio = serializers.URLField()

    class Meta:
        model = StudentResume
        fields = [
            "user_id",
            "username",
            "first_name",
            "last_name",
            "email",
            "photo",
            "date_of_birth",
            "education_level",
            "location",
            "work_experience",
            "grade",
            "description",
            "resume",
            "achievement",
            "portfolio",
            "contact_info",
            "academic_status",
            "employment_status",
            "skills",
            "has_higher_education",
            "has_participated_in_hackathons",
            "has_personal_projects",
            "skills_verified",
            "has_video_presentation",
            "percentage_match",
            "viewed",
        ]
