# Общие константы
NAME_LEN = 150
PHONE_LEN = 20
MAIL_LEN = 254
TELEGRAM_LEN = 100
BASIC_LEN = 100

# Выборы для учебного статуса студентов
ACADEMIC_STATUS_CHOICES = [
    ("student", "Студент"),
    ("academic_leave", "Академический отпуск"),
    ("graduate", "Выпускник"),
    ("expelled", "Отчислен"),
]

# Выборы для статуса трудоустройства студентов
EMPLOYMENT_STATUS_CHOICES = [
    ("job_search", "Ищу работу"),
    ("employed", "Трудоустроен"),
    ("internship_search", "В поиске стажировки"),
    ("other", "Другое"),
]

# Статусы для откликов
APPLICATION_STATUS_CHOICES = [
    ("pending", "В ожидании"),
    ("approved", "Одобрено"),
    ("rejected", "Отклонено"),
]

# Статусы для вакансий
VACANCY_STATUS_CHOICES = [
    ("open", "Открыта"),
    ("closed", "Закрыта"),
]

# Выбор грейда
GRADE_CHOICES = [
    ("junior", "Junior"),
    ("middle", "Middle"),
]

# Уровень образования
EDUCATION_LEVELS = [
    ("school", "Среднее образование"),
    ("college", "Средне-специальное образование"),
    ("university", "Высшее образование"),
    ("postgrad", "Ученая степень"),
]


POSITION_LIST = [
    ("frontend_dev", "Фронтенд-разработчик"),
    ("fullstack_dev", "Фулстек-разработчик"),
    ("python_dev", "Python-разработчик"),
    ("qa_engineer", "Инженер по тестированию"),
    ("java_dev", "Java-разработчик"),
    ("data_scientist", "Специалист по data-science"),
    ("designer", "Дизайнер интерфейсов"),
    ("product_designer", "Продуктовый дизайнер"),
    ("project_manager", "Менеджер проектов"),
]

SPECIALIZATION_SKILLS = {
    "frontend_dev": ["HTML", "CSS", "JavaScript"],
    "fullstack_dev": ["HTML", "CSS", "JavaScript", "Python", "Django"],
    "python_dev": ["Python"],
    "qa_engineer": ["Manual Testing", "Automation Testing"],
    "java_dev": ["Java", "Spring Framework"],
    "data_scientist": ["Data Analysis", "Machine Learning", "Python"],
}
EXPERIENCE_CHOICES = [
    ("no_experience", "Нет опыта"),
    ("1_to_3_years", "От 1 года до 3 лет"),
    ("3_to_6_years", "От 3 до 6 лет"),
    ("more_than_6_years", "Более 6 лет"),
]
