## Запуск проекта в контейнерах
- Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:HR-filter/backend.git
cd backend
```

### Переход в папку с docker-compose для запуска контейнеров (доступ по http://localhost/api/v1/)
```
cd infra/
```
- Создать файл .env и прописать в него свои данные.
Пример:
```
DJANGO_SECRET_KEY= 'django-insecure-example-seckret-key'
```
Запуск проекта
```
docker-compose up -d
```
Создание суперпользователя
```
docker-compose exec backend python manage.py createsuperuser
```