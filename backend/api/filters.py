import django_filters

from students.models import StudentResume


class StudentResumeFilter(django_filters.FilterSet):
    has_higher_education = django_filters.BooleanFilter(
        field_name="has_higher_education"
    )
    has_participated_in_hackathons = django_filters.BooleanFilter(
        field_name="has_participated_in_hackathons"
    )
    has_personal_projects = django_filters.BooleanFilter(
        field_name="has_personal_projects"
    )
    skills_verified = django_filters.BooleanFilter(
        field_name="skills_verified"
    )
    has_video_presentation = django_filters.BooleanFilter(
        field_name="has_video_presentation"
    )

    class Meta:
        model = StudentResume
        fields = {
            "training_status": ["exact"],
            "academic_status": ["exact"],
            "grade": ["exact"],
            "work_experience": ["exact"],
            "location__name": ["exact"],
            "employment_status__name": ["exact"],
        }
