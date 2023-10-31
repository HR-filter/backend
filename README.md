
 ## Карьерный Трекер (Хакатон)
---
Карьерный Трекер - это проект, созданный для отслеживания и управления информацией о студентах и их академическом и профессиональном развитии. Это приложение предоставляет возможности для хранения резюме студентов, фильтрации резюме по различным критериям, а также управления избранными резюме. Проект разработан на платформе Django REST framework.
***
## Технологии
- Python 3.10
- Django 3.2.3
- Django REST framework 3.12.4
- Nginx
- Docker
- Postgres
- Pytest 
***

### Инструкции по установке и запуску:

**Шаг 1: Склонируйте репозиторий и настройте окружение:**
```bash
git clone https://git@github.com:HR-filter/backend.git
cd backend/
# сделайте копию файла <.env.template> в <.env>
cp -i .env.template .env
 ```

**Шаг 2: Запустите приложение с помощью Docker:**
 ```bash
 cd foodgram-project-react/infra
docker compose up -d
# Создаем суперпользователя 
docker compose -f docker-compose.yml exec backend python manage.py createsuperuser
```
***
**Проект будет доступен по адресу -  http://localhost/**
***
**Доступные команды**
- python manage.py load_fixtures - загрузите фикстуры
- python -m pytest - запустить тесты


## Документация API
Документация API предоставляет подробное описание и схему запросов и ответов, которые можно использовать для взаимодействия с вашим приложением.
Вот основные конечные точки API и как к ним обратиться:

#### ***Адрес документации API***:
* Документация API доступна по адресу http://localhost/api/v1/redoc
* Здесь вы найдете подробные сведения о каждом эндпоинте, поддерживаемых методах и структуре запросов и ответов.
#### ***Регистрация и аутентификация***:
* Для доступа к большинству функций API, вам потребуется аутентифицироваться. Вы можете зарегистрировать нового пользователя через эндпоинт POST /api/v1/users/. После успешной регистрации вы можете получить токен доступа по адресу /api/v1/auth/token/login, который необходимо передавать в заголовке Authorization для аутентификации в последующих запросах.
#### ***Примеры запросов API:***
* *Получение списка резюме:*
```GET /api/v1/resume/```
Этот запрос позволяет получить список всех доступных резюме. 


```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "user": {
                "email": "a@a.ru",
                "id": 1,
                "username": "Test_user_one",
                "first_name": "Тест",
                "last_name": "Тестов"
            },
            "age": 12,
            "photo": null,
            "contact_info": {
                "phone_number": "+12345647778",
                "alternate_email": "test@test.test",
                "telegram_login": "@test"
            },
            "academic_status": {
                "id": 3,
                "name": "Выпускник"
            },
            "employment_status": {
                "id": 1,
                "name": "Ищу работу"
            },
            "grade": {
                "id": 1,
                "name": "Junior"
            },
            "work_experience": [
                {
                    "id": 1,
                    "name": "ООО ТЕСТ",
                    "position": "Рабочий",
                    "start_date": "2015-10-03",
                    "end_date": null,
                    "description": "Делал дела",
                    "total_experience_months": 96
                }
            ],
            "location": {
                "id": 1,
                "name": "Москва"
            },
            "portfolio": [
                {
                    "id": 1,
                    "url": "https://guest.link/czd"
                }
            ],
            "languages": [
                {
                    "id": 2,
                    "name": "Английский A2"
                }
            ],
            "educations": [
                {
                    "institution": "Университет УМСС",
                    "specialization": "Инженер технолог",
                    "education_level": "Средне-специальное образование"
                }
            ],
            "description": "Тестовое описание",
            "specialization": {
                "id": 3,
                "name": "Python-разработчик"
            },
            "projects": [
                {
                    "id": 1,
                    "title": "MY PET",
                    "description": "Описание тут"
                }
            ],
            "courses": [
                {
                    "id": 3,
                    "name": "Яндекс Практикум",
                    "specialization": {
                        "id": 3,
                        "name": "Python-разработчик"
                    },
                    "skills": [
                        {
                            "id": 21,
                            "name": "Python"
                        },
                        {
                            "id": 22,
                            "name": "Django"
                        },
                        {
                            "id": 23,
                            "name": "GitHub"
                        },
                        {
                            "id": 24,
                            "name": "SQL"
                        },
                        {
                            "id": 25,
                            "name": "Bash"
                        },
                        {
                            "id": 26,
                            "name": "Nginx"
                        },
                        {
                            "id": 27,
                            "name": "Gunicorn"
                        },
                        {
                            "id": 28,
                            "name": "Docker Hub"
                        },
                        {
                            "id": 29,
                            "name": "DevTools"
                        },
                        {
                            "id": 30,
                            "name": "Charles"
                        }
                    ]
                }
            ],
            "has_higher_education": false,
            "has_participated_in_hackathons": false,
            "has_personal_projects": true,
            "skills_verified": false,
            "has_video_presentation": false,
            "percentage_match": 0,
            "viewed": false,
            "is_favorited": false
        }
    ]
}
```
* *Пример фильтрации резюме:*
```GET /api/v1/resume/?```
Этот запрос позволяет получить список всех доступных резюме. 
Запрос:
```GET /api/v1/resume/?grade=1```

```bash
 {
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "user": {
                "email": "a@a.ru",
                "id": 1,
                "username": "Test_user_one",
                "first_name": "Тест",
                "last_name": "Тестов"
            },
            "grade": {
                "id": 1,
                "name": "Junior"
            },
            // ... (другие поля резюме)
            "percentage_match": 100
        }
    ]
}

```
Здесь отображаются только резюме с оценкой "Junior", и в поле percentage_match указывается 100, что означает идеальное соответствие.

При запросе  ```GET /api/v1/resume/?grade=1&academic_status=2``` фильтруются по оценке "Junior" и статусу "Выпускник". Поле percentage_match указывает на 50, что означает близкое соответствие вашим требованиям.
Таким образом, вы можете использовать фильтры API для быстрого и удобного поиска резюме, которые соответствуют вашим критериям. Это делает ваши поисковые запросы более эффективными и удобными.
 ```bash
 GET /api/v1/resume/?grade=1
 {
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "user": {
                "email": "a@a.ru",
                "id": 1,
                "username": "Test_user_one",
                "first_name": "Тест",
                "last_name": "Тестов"
            },
            "grade": {
                "id": 1,
                "name": "Junior"
            },
             "academic_status": {
                "id": 3,
                "name": "Выпускник"
            },
            // ... (другие поля резюме)
            "percentage_match": 50
        }
    ]
}
```
Все доступные поля для фильтрации находяться по следющим адресам:
```GET /api/v1/filters/```
```GET /api/v1/boolean-filters/```

 ## Авторы

Авторы проекта (backend):

- **Владислав Казьмин** - [GitHub](https://github.com/vlkazmin)
- **Анастасия** - [GitHub](https://github.com/Anastasia7Si)

 
 
 
 
 
 
 
 
 
 
 
 
 
 

