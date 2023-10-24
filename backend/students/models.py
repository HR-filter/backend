from django.contrib.auth import get_user_model
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from core.texts import (
    ACADEMIC_STATUS_CHOICES,
    EDUCATION_LEVELS,
    EMPLOYMENT_STATUS_CHOICES,
    GRADE_CHOICES,
    POSITION_LIST,
    NAME_LEN,
    PHONE_LEN,
    MAIL_LEN,
    TELEGRAM_LEN,
    BASIC_LEN,
    EXPERIENCE_CHOICES,
)

User = get_user_model()


class ContactInfo(models.Model):
    """
    Модель для контактной информации.
    """

    phone_number = PhoneNumberField(
        max_length=PHONE_LEN,
        unique=True,
        verbose_name="Номер телефона",
    )
    alternate_email = models.EmailField(
        max_length=MAIL_LEN,
        unique=True,
        verbose_name="Дополнительный адрес электронной почты",
    )
    telegram_login = models.CharField(
        max_length=TELEGRAM_LEN,
        blank=True,
        null=True,
        verbose_name="Логин в Telegram",
    )

    def __str__(self):
        return self.alternate_email

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Skill(models.Model):
    """
    Модель для навыков.
    """

    name = models.CharField(max_length=BASIC_LEN)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"


class AcademicStatus(models.Model):
    """
    Модель для статуса обучения.
    """

    name = models.CharField(
        max_length=NAME_LEN,
        choices=ACADEMIC_STATUS_CHOICES,
    )

    def __str__(self):
        return dict(ACADEMIC_STATUS_CHOICES).get(self.name, self.name)

    class Meta:
        verbose_name = "Академический статус"
        verbose_name_plural = "Академические статусы"


class EmploymentStatus(models.Model):
    """
    Модель для статуса трудоустройства.
    """

    name = models.CharField(
        max_length=BASIC_LEN,
        choices=EMPLOYMENT_STATUS_CHOICES,
    )

    def __str__(self):
        return dict(EMPLOYMENT_STATUS_CHOICES).get(self.name, self.name)

    class Meta:
        verbose_name = "Статус трудоустройства"
        verbose_name_plural = "Статусы трудоустройства"


class Position(models.Model):
    """
    Модель выбора ожидаемой должности.
    """

    name = models.CharField(
        max_length=BASIC_LEN,
        choices=POSITION_LIST,
    )

    def __str__(self):
        return dict(POSITION_LIST).get(self.name, self.name)

    class Meta:
        verbose_name = "Ожидаемая должность"
        verbose_name_plural = "Ожидаемые должности"


class StudentPosition(models.Model):
    """Промежуточная модель для связи между студентом и позицией"""

    student = models.ForeignKey(
        "StudentResume",
        on_delete=models.CASCADE,
        related_name="student_positions",
        verbose_name="Студент",
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        verbose_name="Позиция",
    )
    academic_status = models.ForeignKey(
        AcademicStatus,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Учебный статус",
    )

    def __str__(self):
        return f"{self.student} - {self.position}"


class WorkExperience(models.Model):
    name = models.CharField(
        max_length=BASIC_LEN,
        choices=EXPERIENCE_CHOICES,
        verbose_name="Опыт работы",
    )

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(
        max_length=BASIC_LEN,
        choices=GRADE_CHOICES,
        verbose_name="Грейд",
    )

    def __str__(self):
        return dict(GRADE_CHOICES).get(self.name, self.name)


class Location(models.Model):
    name = models.CharField(
        max_length=BASIC_LEN,
        verbose_name="Местоположение",
    )

    def __str__(self):
        return self.name


class StudentResume(models.Model):
    """
    Расширенная модель пользователя для студента.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_resume",
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата рождения",
    )
    education_level = models.CharField(
        max_length=100,
        choices=EDUCATION_LEVELS,
        blank=True,
        null=True,
        verbose_name="Уровень образования",
    )
    contact_info = models.OneToOneField(
        ContactInfo,
        on_delete=models.CASCADE,
        verbose_name="Контактная информация",
    )
    skills = models.ManyToManyField(
        Skill,
        related_name="students",
        blank=True,
        verbose_name="Навыки",
    )
    academic_status = models.ForeignKey(
        AcademicStatus,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Учебный статус",
    )
    employment_status = models.ForeignKey(
        EmploymentStatus,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Статус трудоустройства",
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    work_experience = models.ForeignKey(
        WorkExperience,
        default="no_experience",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    grade = models.ForeignKey(
        Grade,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    training_status = models.ManyToManyField(
        Position,
        through=StudentPosition,
        verbose_name="Предпочтительные должности",
        blank=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="О себе",
    )

    photo = models.ImageField(
        upload_to="student_photos/",
        blank=True,
        null=True,
        verbose_name="Фото",
    )

    resume = models.FileField(
        upload_to="student_resumes/",
        blank=True,
        null=True,
        verbose_name="Резюме",
    )

    REQUIRED_FIELDS = [
        "date_of_birth",
        "contact_info__phone_number",
    ]

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"


class FavoriteResume(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorite_by",
    )
    resume = models.ForeignKey(
        StudentResume,
        on_delete=models.CASCADE,
        related_name="favorited_resumes",
    )
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные резюме"
        constraints = [
            models.UniqueConstraint(
                fields=("user", "resume"), name="unique_user_resume"
            )
        ]
