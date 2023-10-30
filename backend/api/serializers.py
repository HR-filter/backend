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
    Language,
    Education,
    Project,
    Specialization,
    Course,
    PortfolioLink,
    FavoriteResume,
    Experience,
)
from datetime import datetime


class UserSerializer(UserCreateSerializer):
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
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ["phone_number", "alternate_email", "telegram_login"]


class BaseSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {"id": instance.id, "name": str(instance)}


class AcademicStatusSerializer(BaseSerializer):
    pass


class SkillSerializer(BaseSerializer):
    pass


class SpecializationStatusSerializer(BaseSerializer):
    pass


class EmploymentStatusSerializer(BaseSerializer):
    pass


class WorkExperienceSerializer(serializers.ModelSerializer):
    total_experience_months = serializers.SerializerMethodField()

    class Meta:
        model = WorkExperience
        fields = [
            "id",
            "name",
            "position",
            "start_date",
            "end_date",
            "description",
            "total_experience_months",
        ]

    def get_total_experience_months(self, obj):
        start_date = obj.start_date
        end_date = obj.end_date if obj.end_date else datetime.today().date()
        experience_months = (end_date.year - start_date.year) * 12 + (
            end_date.month - start_date.month
        )
        return experience_months


class ExperienceSerializer(BaseSerializer):
    class Meta:
        model = Experience
        fields = [
            "id",
            "name",
        ]


class GradeSerializer(BaseSerializer):
    pass


class LocationSerializer(BaseSerializer):
    pass


class LanguageSerializer(BaseSerializer):
    pass


class EducationSerializer(serializers.ModelSerializer):
    education_level = serializers.CharField(
        source="get_education_level_display"
    )

    class Meta:
        model = Education
        fields = ["institution", "specialization", "education_level"]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "title", "description"]


class CourseSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    specialization = SpecializationStatusSerializer()

    class Meta:
        model = Course
        fields = ["id", "name", "specialization", "skills"]


class PortfolioLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioLink
        fields = ["id", "url"]


class StudentResumeSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    is_favorited = serializers.SerializerMethodField()
    photo = Base64ImageField()
    user = UserSerializer(read_only=True)
    contact_info = ContactInfoSerializer()
    academic_status = AcademicStatusSerializer()
    employment_status = EmploymentStatusSerializer()
    grade = GradeSerializer()
    work_experience = WorkExperienceSerializer(many=True)
    location = LocationSerializer()
    portfolio = PortfolioLinkSerializer(many=True)
    languages = LanguageSerializer(many=True)
    educations = EducationSerializer(many=True)
    projects = ProjectSerializer(many=True)
    specialization = SpecializationStatusSerializer()
    percentage_match = serializers.IntegerField(read_only=True, default=0)
    courses = CourseSerializer(many=True)

    class Meta:
        model = StudentResume
        fields = [
            "user",
            "age",
            "photo",
            "contact_info",
            "academic_status",
            "employment_status",
            "grade",
            "work_experience",
            "location",
            "portfolio",
            "languages",
            "educations",
            "description",
            "specialization",
            "projects",
            "courses",
            "has_higher_education",
            "has_participated_in_hackathons",
            "has_personal_projects",
            "skills_verified",
            "has_video_presentation",
            "percentage_match",
            "viewed",
            "is_favorited",
        ]

    def get_age(self, obj):
        if obj.date_of_birth:
            birth_date = obj.date_of_birth
            today = datetime.today()
            age = (
                today.year
                - birth_date.year
                - (
                    (today.month, today.day)
                    < (birth_date.month, birth_date.day)
                )
            )
            return age
        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")
        if request.method == "GET":
            data["user"].pop("password", None)
        return data

    def get_is_favorited(self, instance):
        user = self.context.get("request").user
        if user.is_authenticated:
            return instance.favorites.filter(
                user=user, resume=instance
            ).exists()
        return False


class FavoriteSerializer(serializers.ModelSerializer):
    """Серилизатор для избранных резюме."""

    class Meta:
        fields = ("resume", "user")
        model = FavoriteResume
