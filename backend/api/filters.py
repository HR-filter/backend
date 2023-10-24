import django_filters

from students.models import StudentResume


class StudentResumeFilter(django_filters.FilterSet):
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
