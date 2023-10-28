from django.contrib import admin
from .models import (
    StudentResume,
    ContactInfo,
    Skill,
    AcademicStatus,
    EmploymentStatus,
    FavoriteResume,
    Location,
    WorkExperience,
    Grade,
    Specialization,
    Course,
    Language,
    Education,
    Project,
    PortfolioLink,
)


class EducationInline(admin.TabularInline):
    model = StudentResume.educations.through
    extra = 1


class LanguagesInline(admin.TabularInline):
    model = StudentResume.languages.through
    extra = 1


class PortfolioInline(admin.TabularInline):
    model = StudentResume.portfolio.through
    extra = 1


class ProjectsInline(admin.TabularInline):
    model = StudentResume.projects.through
    extra = 1


class WorkExperienceInline(admin.TabularInline):
    model = StudentResume.work_experience.through
    extra = 1


@admin.register(StudentResume)
class StudentUserAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "date_of_birth",
        "academic_status",
        "grade",
        "employment_status",
        "location",
        "specialization",
    )
    search_fields = (
        "user__first_name",
        "user__last_name",
        "contact_info__alternate_email",
        "location__name",
    )
    list_filter = ("grade",)
    inlines = [
        LanguagesInline,
        ProjectsInline,
        EducationInline,
        PortfolioInline,
        WorkExperienceInline,
    ]

    fieldsets = (
        (
            "Персональная информация",
            {
                "fields": (
                    "user",
                    "date_of_birth",
                    "description",
                    "photo",
                    "location",
                )
            },
        ),
        (
            "Контактная информация",
            {"fields": ("contact_info",)},
        ),
        (
            "Информация об образовании",
            {"fields": ("academic_status",)},
        ),
        (
            "Трудоустройство и Специализация",
            {
                "fields": (
                    "specialization",
                    "courses",
                    "employment_status",
                    "grade",
                    "experience",
                )
            },
        ),
        (
            "Дополнительная информация",
            {
                "fields": (
                    "has_higher_education",
                    "has_participated_in_hackathons",
                    "has_personal_projects",
                    "skills_verified",
                    "has_video_presentation",
                )
            },
        ),
    )


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "alternate_email", "telegram_login")
    search_fields = ("alternate_email", "phone_number")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(AcademicStatus)
class AcademicStatusAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(EmploymentStatus)
class EmploymentStatusAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(FavoriteResume)
class FavoriteResumeAdmin(admin.ModelAdmin):
    list_display = ("user", "resume", "date_added")
    search_fields = ("user__username", "resume__user__username")


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("specialization",)
    search_fields = ("specialization__name",)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("institution", "specialization", "education_level")
    search_fields = ("institution", "specialization")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title", "description")


@admin.register(PortfolioLink)
class PortfolioLinkAdmin(admin.ModelAdmin):
    list_display = ("url",)
    search_fields = ("url",)


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "start_date",
        "description",
    )
    search_fields = (
        "name",
        "start_date",
        "description",
    )
