from django.contrib import admin
from .models import (
    StudentResume,
    ContactInfo,
    Skill,
    AcademicStatus,
    EmploymentStatus,
    StudentPosition,
    Position,
    FavoriteResume,
)


class StudentPositionInline(admin.TabularInline):
    model = StudentPosition
    extra = 1


@admin.register(StudentResume)
class StudentUserAdmin(admin.ModelAdmin):
    list_display = (
        "get_full_name",
        "date_of_birth",
        "education_level",
        "grade",
        "academic_status",
        # "specialization",
        "work_experience",
        "employment_status",
        "city",
    )
    search_fields = (
        "user__first_name",
        "user__last_name",
        "student_resume__contact_info__alternate_email",
        "city",
        "specialization",
    )

    list_filter = ("grade",)
    inlines = [StudentPositionInline]

    def get_full_name(self, obj):
        return obj.user.get_full_name()

    get_full_name.short_description = "Имя Отвечство"

    def grade(self, obj):
        return obj.student_info.grade


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("alternate_email", "phone_number", "telegram_login")
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


@admin.register(Position)
class PositionStatusAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(FavoriteResume)
class FavoriteResumeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "resume",
        "date_added",
    )
    search_fields = (
        "user",
        "resume",
        "date_added",
    )