from core.texts import EXPERIENCE_CHOICES

from djoser.serializers import UserCreateSerializer

from drf_extra_fields.fields import Base64ImageField

from rest_framework import serializers

from students.models import (
    AcademicStatus,
    ContactInfo,
    EmploymentStatus,
    Grade,
    Location,
    Position,
    Skill,
    StudentPosition,
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


class StudentPositionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели StudentPosition, предоставляет имена позиции
    и академического статуса.
    """

    position_name = serializers.StringRelatedField(
        source="position", read_only=True
    )
    academic_status_name = serializers.StringRelatedField(
        source="academic_status", read_only=True
    )

    class Meta:
        model = StudentPosition
        fields = [
            "id",
            "position_name",
            "academic_status_name",
        ]


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


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            "id",
            "name",
        ]


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = [
            "id",
            "name",
        ]


class AcademicStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicStatus
        fields = ["id", "name"]


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ["id", "name"]


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ["id", "name"]

    def to_representation(self, instance):
        experience_dict = dict(EXPERIENCE_CHOICES)
        return {
            "id": instance.id,
            "name": experience_dict.get(instance.name, instance.name),
        }


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "name"]


class EmploymentStatusSerializer(serializers.ModelSerializer):
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
    training_status = StudentPositionSerializer(
        many=True, source="student_positions"
    )
    academic_status = AcademicStatusSerializer()
    employment_status = EmploymentStatusSerializer()
    skills = SkillSerializer(many=True)
    grade = GradeSerializer()
    work_experience = WorkExperienceSerializer()
    location = LocationSerializer()

    class Meta:
        model = StudentResume
        fields = [
            "user_id",
            "username",
            "first_name",
            "last_name",
            "email",
            "photo",
            "training_status",
            "date_of_birth",
            "education_level",
            "location",
            "work_experience",
            "grade",
            "description",
            "resume",
            "contact_info",
            "academic_status",
            "employment_status",
            "skills",
        ]
