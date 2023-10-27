import django_filters
from django.db.models import (
    Case,
    IntegerField,
    Value,
    When,
    Sum,
)
from students.models import StudentResume


class StudentResumeFilter(django_filters.FilterSet):
    class Meta:
        model = StudentResume
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        queryset = StudentResume.objects.all()

        filter_params = {
            "grade": "grade",
            "academic_status": "academic_status",
            "work_experience": "work_experience",
            "location": "location",
            "employment_status": "employment_status",
            "has_higher_education": "has_higher_education",
            "has_participated_in_hackathons": "has_participated_in_hackathons",
            "has_personal_projects": "has_personal_projects",
            "skills_verified": "skills_verified",
            "has_video_presentation": "has_video_presentation",
        }

        sum_expression = None
        num_params = len(self.request.query_params)

        for param, field_name in filter_params.items():
            param_value = self.request.query_params.get(param)
            if param_value is not None:
                case_statement = Case(
                    When(**{field_name: param_value}, then=Value(1)),
                    default=Value(0),
                    output_field=IntegerField(),
                )
                if sum_expression is None:
                    sum_expression = Sum(case_statement)
                else:
                    sum_expression = sum_expression + Sum(case_statement)

        if sum_expression is not None:
            queryset = queryset.annotate(matching_params=sum_expression)

            queryset = queryset.annotate(
                percentage_match=sum_expression * 100 / num_params
            )

            queryset = queryset.filter(matching_params__gt=0).order_by(
                "-matching_params"
            )

        self.queryset = queryset
