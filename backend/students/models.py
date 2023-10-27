from django.contrib.auth import get_user_model
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from core.texts import (
    ACADEMIC_STATUS_CHOICES,
    EDUCATION_LEVELS,
    EMPLOYMENT_STATUS_CHOICES,
    GRADE_CHOICES,
    NAME_LEN,
    PHONE_LEN,
    MAIL_LEN,
    TELEGRAM_LEN,
    BASIC_LEN,
    EXPERIENCE_CHOICES,
)

from .utils import student_photo_upload, student_resume_upload

User = get_user_model()


class ContactInfo(models.Model):
    """
    Модель для контактной информации.
    """

    phone_number = PhoneNumberField(
        max_length=PHONE_LEN,
        unique=True,
        verbose_name="Номер телефона",
        help_text="Укажите номер телефона студента.",
    )
    alternate_email = models.EmailField(
        max_length=MAIL_LEN,
        unique=True,
        verbose_name="Дополнительный адрес электронной почты",
        help_text="Укажите дополнительный адрес электронной почты студента.",
    )
    telegram_login = models.CharField(
        max_length=TELEGRAM_LEN,
        blank=True,
        null=True,
        verbose_name="Логин в Telegram",
        help_text="Укажите логин студента в Telegram (при наличии).",
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

    name = models.CharField(
        max_length=BASIC_LEN,
        verbose_name="Наименование навыка",
        help_text="Введите наименование навыка.",
    )

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
        verbose_name="Академический статус",
        help_text="Выберите академический статус студента.",
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
        verbose_name="Статус трудоустройства",
        help_text="Выберите статус трудоустройства студента.",
    )

    def __str__(self):
        return dict(EMPLOYMENT_STATUS_CHOICES).get(self.name, self.name)

    class Meta:
        verbose_name = "Статус трудоустройства"
        verbose_name_plural = "Статусы трудоустройства"


class WorkExperience(models.Model):
    """
    Модель выбора опыта работы.
    """

    name = models.CharField(
        max_length=BASIC_LEN,
        choices=EXPERIENCE_CHOICES,
        verbose_name="Опыт работы",
        help_text="Выберите опыт работы студента.",
    )

    def __str__(self):
        return dict(EXPERIENCE_CHOICES).get(self.name)

    class Meta:
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"


class Grade(models.Model):
    """
    Модель грейда студента.
    """

    name = models.CharField(
        max_length=BASIC_LEN,
        choices=GRADE_CHOICES,
        verbose_name="Грейд",
        help_text="Выберите грейд студента.",
    )

    def __str__(self):
        return dict(GRADE_CHOICES).get(self.name)

    class Meta:
        verbose_name = "Грейд"
        verbose_name_plural = "Грейды"


class Location(models.Model):
    """
    Модель метосоположения.
    """

    name = models.CharField(
        max_length=BASIC_LEN,
        verbose_name="Наименование местоположения",
        help_text="Введите наименование местоположения.",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"


class StudentResume(models.Model):
    """
    Расширенная модель пользователя для студента.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_resume",
        verbose_name="Студент",
        help_text="Выберите пользователя и свяжите его с профилем студента.",
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата рождения",
        help_text="Укажите дату рождения студента (при наличии).",
    )
    education_level = models.CharField(
        max_length=100,
        choices=EDUCATION_LEVELS,
        blank=True,
        null=True,
        verbose_name="Уровень образования",
        help_text="Выберите уровень образования студента (при наличии).",
    )
    contact_info = models.OneToOneField(
        ContactInfo,
        on_delete=models.CASCADE,
        verbose_name="Контактная информация",
        help_text="Выберите контактную информацию для профиля студента.",
    )
    skills = models.ManyToManyField(
        Skill,
        related_name="students",
        blank=True,
        verbose_name="Навыки",
        help_text="Выберите навыки, связанные "
        "с профилем студента (при наличии).",
    )
    academic_status = models.ForeignKey(
        AcademicStatus,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Учебный статус",
        help_text="Выберите учебный статус студента (при наличии).",
    )
    employment_status = models.ForeignKey(
        EmploymentStatus,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Статус трудоустройства",
        help_text="Выберите статус трудоустройства студента (при наличии).",
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Местоположение",
        help_text="Выберите местоположение студента (при наличии).",
    )
    work_experience = models.ForeignKey(
        WorkExperience,
        default="no_experience",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Опыт работы",
        help_text="Выберите опыт работы студента (при наличии).",
    )
    grade = models.ForeignKey(
        Grade,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Грейд",
        help_text="Выберите грейд студента (при наличии).",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="О себе",
        help_text="Введите описание студента (при наличии).",
    )
    photo = models.ImageField(
        upload_to=student_photo_upload,
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фотографию студента (при наличии).",
    )
    resume = models.FileField(
        upload_to=student_resume_upload,
        blank=True,
        null=True,
        verbose_name="Резюме",
        help_text="Загрузите резюме студента (при наличии).",
    )
    achievement = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Достижения",
        help_text="Укажите свои достижения (при наличии)."
    )
    portfolio = models.URLField(
        blank=True,
        null=True,
        verbose_name="Портфолио",
        help_text="Прикрепите ссылку на портфолио (при наличии).",
    )

    has_higher_education = models.BooleanField(
        default=False,
        verbose_name="Высшее образование",
        help_text="Укажите, имеет ли студент высшее образование.",
    )
    has_participated_in_hackathons = models.BooleanField(
        default=False,
        verbose_name="Участие в хакатонах",
        help_text="Укажите, участвовал ли студент в хакатонах.",
    )
    has_personal_projects = models.BooleanField(
        default=False,
        verbose_name="Наличие пет-проектов",
        help_text="Укажите, есть ли у студента пет-проекты.",
    )
    skills_verified = models.BooleanField(
        default=False,
        verbose_name="Навыки подтверждены",
        help_text="Укажите, подтверждены ли навыки студента.",
    )
    has_video_presentation = models.BooleanField(
        default=False,
        verbose_name="С видео-презентацией",
        help_text="Укажите, есть ли у студента видео-презентация.",
    )
    viewed = models.BooleanField(
        default=False,
        verbose_name="Отметка о просмотре",
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
    """
    Модель избранных резюме.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorite_by",
        verbose_name="Пользователь",
        help_text="Выберите пользователя, "
        "который добавляет резюме в избранное.",
    )
    resume = models.ForeignKey(
        StudentResume,
        on_delete=models.CASCADE,
        related_name="favorited_resumes",
        verbose_name="Избранное резюме",
        help_text="Выберите резюме, добавляемое в избранное.",
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления",
        help_text="Дата, когда резюме было добавлено в избранное.",
    )

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные резюме"
        constraints = [
            models.UniqueConstraint(
                fields=("user", "resume"),
                name="unique_user_resume",
            )
        ]
