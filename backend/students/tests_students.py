import pytest

from .models import (
    AcademicStatus,
    ContactInfo,
    EmploymentStatus,
    StudentResume,
    WorkExperience,
    Grade,
    Location,
    Experience,
    Specialization,
    Skill,
    Course,
    Education,
    PortfolioLink,
    Project,
    Language,
    User,
)


@pytest.mark.django_db
def test_create_contact_info():
    """Тест на создание объекта ContactInfo."""
    contact = ContactInfo.objects.create(
        phone_number="1234567890",
        alternate_email="test@example.com",
        telegram_login="test_telegram",
    )
    assert contact.phone_number == "1234567890"
    assert contact.alternate_email == "test@example.com"
    assert contact.telegram_login == "test_telegram"
    assert str(contact) == "test@example.com"


@pytest.mark.django_db
def test_create_employment_status():
    """Тесты для модели EmploymentStatus"""
    status = EmploymentStatus.objects.create(name="Employed")
    assert str(status) == "Employed"


@pytest.mark.django_db
def test_create_academic_status():
    """Тесты для модели AcademicStatus"""
    status = AcademicStatus.objects.create(name="Undergraduate")
    assert str(status) == "Undergraduate"


@pytest.mark.django_db
def test_create_work_experience():
    """Тесты для модели WorkExperience"""
    experience = WorkExperience.objects.create(
        name="Workplace",
        start_date="2023-01-01",
        end_date="2023-12-31",
        position="Employee",
        description="Description of work experience",
    )
    assert experience.name == "Workplace"
    assert experience.position == "Employee"
    assert str(experience) == "Workplace"


@pytest.mark.django_db
def test_create_grade():
    """Тесты для модели Grade"""
    grade = Grade.objects.create(name="junior")
    assert str(grade) == "Junior"


@pytest.mark.django_db
def test_create_location():
    """Тесты для модели Location"""
    location = Location.objects.create(name="Moscow")
    assert str(location) == "Moscow"


@pytest.mark.django_db
def test_create_experience():
    """Тесты для модели Experience"""
    experience = Experience.objects.create(name="no_experience")
    assert str(experience) == "Нет опыта"


@pytest.mark.django_db
def test_create_specialization():
    """Тесты для модели Specialization"""
    specialization = Specialization.objects.create(name="python_dev")
    assert str(specialization) == "Python-разработчик"


@pytest.mark.django_db
def test_create_skill():
    """Тесты для модели Skill"""
    skill = Skill.objects.create(name="Python")
    assert str(skill) == "Python"


@pytest.mark.django_db
def test_create_course():
    """Тесты для модели Course"""
    specialization = Specialization.objects.create(name="Web Developer")
    course = Course.objects.create(
        name="Python Course", specialization=specialization
    )
    skill = Skill.objects.create(name="Python")
    course.skills.add(skill)
    assert str(course) == "Web Developer"


@pytest.mark.django_db
def test_create_portfolio_link():
    """Тесты для модели PortfolioLink"""
    link = PortfolioLink.objects.create(url="https://example.com")
    assert str(link) == "https://example.com"


@pytest.mark.django_db
def test_create_project():
    """Тесты для модели Project"""
    project = Project.objects.create(
        title="Sample Project",
        description="Description of the sample project.",
    )
    assert str(project) == "Sample Project"


@pytest.mark.django_db
def test_create_language():
    """Тесты для модели Language"""
    language = Language.objects.create(name="English (Advanced)")
    assert str(language) == "English (Advanced)"


@pytest.mark.django_db
def test_create_education():
    """Тесты для модели Education"""
    education = Education.objects.create(
        institution="University",
        specialization="Computer Science",
        education_level="college",
    )
    assert str(education) == "Средне-специальное образование"


@pytest.fixture
def user():
    """Фикстура для создания объекта User."""
    user = User.objects.create(username="testuser")
    return user


@pytest.fixture
def contact_info():
    contact_info = ContactInfo.objects.create(phone_number="1234567890")
    return contact_info


@pytest.mark.django_db
def test_create_student_resume(user, contact_info):
    """Фикстура для создания объекта ContactInfo."""
    student_resume = StudentResume.objects.create(
        user=user,
        contact_info=contact_info,
        date_of_birth="2000-01-01",
    )
    assert student_resume.user.username == "testuser"
    assert student_resume.contact_info.phone_number == "1234567890"


@pytest.mark.django_db
def test_add_specialization_and_courses(user, contact_info):
    """Тест на создание объекта StudentResume и связанных с ним объектов."""
    specialization = Specialization.objects.create(name="Web Development")
    course1 = Course.objects.create(
        name="Web Development Course 1", specialization=specialization
    )
    course2 = Course.objects.create(
        name="Web Development Course 2", specialization=specialization
    )

    student_resume = StudentResume.objects.create(
        user=user, contact_info=contact_info
    )
    student_resume.specialization = specialization
    student_resume.courses.add(course1, course2)
    student_resume.save()

    assert student_resume.specialization.name == "Web Development"
    assert list(student_resume.courses.all()) == [course1, course2]


@pytest.mark.django_db
def test_add_projects_and_languages(user, contact_info):
    """Тест на создание объекта StudentResume и kabguages"""
    project1 = Project.objects.create(
        title="Project 1", description="Description of Project 1"
    )
    project2 = Project.objects.create(
        title="Project 2", description="Description of Project 2"
    )
    language1 = Language.objects.create(name="English")
    language2 = Language.objects.create(name="Spanish")

    student_resume = StudentResume.objects.create(
        user=user, contact_info=contact_info
    )
    student_resume.projects.add(project1, project2)
    student_resume.languages.add(language1, language2)
    student_resume.save()

    assert list(student_resume.projects.all()) == [project1, project2]
    assert list(student_resume.languages.all()) == [language1, language2]


@pytest.mark.django_db
def test_add_education(user, contact_info):
    """Тест для связи с моделью Education"""
    education = Education.objects.create(
        institution="University", specialization="Computer Science"
    )
    student_resume = StudentResume.objects.create(
        user=user, contact_info=contact_info
    )
    student_resume.educations.add(education)
    student_resume.save()

    assert list(student_resume.educations.all()) == [education]


@pytest.mark.django_db
def test_set_flags(user, contact_info):
    """Тесты для флагов"""
    student_resume = StudentResume.objects.create(
        user=user, contact_info=contact_info
    )
    student_resume.has_higher_education = True
    student_resume.has_participated_in_hackathons = False
    student_resume.has_personal_projects = True
    student_resume.skills_verified = True
    student_resume.has_video_presentation = False
    student_resume.save()

    assert student_resume.has_higher_education is True
    assert student_resume.has_participated_in_hackathons is False
    assert student_resume.has_personal_projects is True
    assert student_resume.skills_verified is True
    assert student_resume.has_video_presentation is False


@pytest.mark.django_db
def test_add_portfolio_links(user, contact_info):
    """Тест для связи с моделью PortfolioLink"""
    link1 = PortfolioLink.objects.create(url="https://portfolio1.com")
    link2 = PortfolioLink.objects.create(url="https://portfolio2.com")

    student_resume = StudentResume.objects.create(
        user=user, contact_info=contact_info
    )
    student_resume.portfolio.add(link1, link2)
    student_resume.save()

    assert list(student_resume.portfolio.all()) == [link1, link2]


@pytest.mark.django_db
def test_set_location_and_education(user, contact_info):
    """Тест для связи с моделью Location и Education"""
    location = Location.objects.create(name="City A")
    education = Education.objects.create(
        institution="University", specialization="Computer Science"
    )

    student_resume = StudentResume.objects.create(
        user=user, contact_info=contact_info
    )
    student_resume.location = location
    student_resume.educations.add(education)
    student_resume.save()

    assert student_resume.location == location
    assert list(student_resume.educations.all()) == [education]


@pytest.mark.django_db
def test_set_description(user, contact_info):
    """Тест поля description_text"""
    description_text = "I am a dedicated and passionate student."
    student_resume = StudentResume.objects.create(
        user=user, contact_info=contact_info
    )
    student_resume.description = description_text
    student_resume.save()

    assert student_resume.description == description_text


@pytest.mark.django_db
def test_set_resume(user, contact_info):
    """Тест поля resume_path"""
    resume_path = "path/to/resume.pdf"
    student_resume = StudentResume.objects.create(
        user=user, contact_info=contact_info
    )
    student_resume.resume = resume_path
    student_resume.save()

    assert student_resume.resume == resume_path
