import tempfile

import pytest

from django.core.files.uploadedfile import SimpleUploadedFile

from .models import (
    AcademicStatus,
    ContactInfo,
    EmploymentStatus,
    Position,
    StudentResume,
    User,
)


@pytest.fixture()
def user_data():
    return {
        "username": "testuser",
        "first_name": "Test",
        "last_name": "User",
        "email": "test@example.com",
    }


@pytest.fixture()
def user(user_data):
    return User.objects.create(**user_data)


@pytest.fixture()
def contact_info_data():
    return {
        "phone_number": "+123456789",
        "alternate_email": "alternate@example.com",
        "telegram_login": "@testuser",
    }


@pytest.fixture()
def contact_info(contact_info_data):
    return ContactInfo.objects.create(**contact_info_data)


@pytest.fixture()
def position_data():
    return {"name": "Fullstack Developer"}


@pytest.fixture()
def position(position_data):
    return Position.objects.create(**position_data)


@pytest.fixture()
def academic_status_data():
    return {"name": "Academic Leave"}


@pytest.fixture()
def academic_status(academic_status_data):
    return AcademicStatus.objects.create(**academic_status_data)


@pytest.fixture()
def employment_status_data():
    return {"name": "Job Search"}


@pytest.fixture()
def employment_status(employment_status_data):
    return EmploymentStatus.objects.create(**employment_status_data)


@pytest.fixture()
def student_data(
    user,
    contact_info,
    academic_status,
    employment_status,
):
    return {
        "user": user,
        "date_of_birth": "2000-01-01",
        "education_level": "college",
        "contact_info": contact_info,
        "academic_status": academic_status,
        "employment_status": employment_status,
        "city": "Test City",
        "work_experience": "Some experience",
        "grade": "junior",
    }


@pytest.fixture()
def student(student_data):
    return StudentResume.objects.create(**student_data)


@pytest.fixture()
def temporary_file():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        return SimpleUploadedFile(temp_file.name, b"file_content")


@pytest.fixture()
def student_with_photo(student_data, temporary_file):
    student_data["photo"] = temporary_file
    return StudentResume.objects.create(**student_data)


@pytest.mark.django_db
def test_create_student_user(
    user,
    contact_info,
    position,
    academic_status,
    employment_status,
):
    student_data = {
        "user": user,
        "date_of_birth": "2000-01-01",
        "education_level": "college",
        "contact_info": contact_info,
        "academic_status": academic_status,
        "employment_status": employment_status,
        "city": "Test City",
        "work_experience": "Some experience",
        "grade": "junior",
    }

    student = StudentResume(**student_data)
    student.save()

    assert student.user.username == "testuser"


@pytest.mark.django_db
def test_student_user_photo_upload(student_with_photo):
    assert student_with_photo.photo.name.startswith("student_photos/")
    assert student_with_photo.photo.size > 0


@pytest.mark.django_db
def test_student_user_display_values():
    academic_status = AcademicStatus(name="Academic Leave")
    employment_status = EmploymentStatus(name="Job Search")
    position = Position(name="Fullstack Developer")

    assert academic_status.__str__() == "Academic Leave"
    assert employment_status.__str__() == "Job Search"
    assert position.__str__() == "Fullstack Developer"


@pytest.mark.django_db
def test_student_user_str_representation(user, contact_info):
    student_data = {
        "user": user,
        "date_of_birth": "2000-01-01",
        "education_level": "college",
        "contact_info": contact_info,
        "city": "Test City",
    }

    student = StudentResume(**student_data)
    student.save()

    assert student.__str__() == "Test User"


@pytest.mark.django_db
def test_student_user_creation_db(student_data):
    student = StudentResume(**student_data)
    student.save()

    assert StudentResume.objects.count() == 1
