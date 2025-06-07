# Проект GPT Project
## Описание проекта:
**GPT Project** - Это инновационный проект, созданный для автоматического преобразования текста, шаблонов и фотографий в высококачественные изображения. Сервис позволяет пользователям создавать уникальные визуализации, основываясь исключительно на текстовых описаниях, образцах дизайна или исходных изображениях.
## Стек:
- Python 3.9
- Django 3.2
- Django REST Framework 3.12
- OpenAI
- Bootstrap
## Возможности:
- Генерация изображений по текстовым описаниям
- Создание дизайнов на основе заданных шаблонов
- Трансформация существующих изображений в новые форматы и стили
- Статистика запросов к API в админ панели
## Установка и запуск:
1. Клонировать репозиторий и перейти в него:
```
git clone https://github.com/sijey06/project_gpt.git
```
```
cd project_gpt
```
2. Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
```
python -m pip install --upgrade pip
```
1. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
2. Создать и применить миграции:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
3. Запустить проект:
```
python manage.py runserver
```
## Примеры запросов к API
### Аутентификация
Для доступа к API необходимо передавать токен в заголовке каждого запроса:
```Authorization: Token <ваш_токен>```
### Получение токена:
`POST /api/get-token/`
Тело запроса:
```
{
    "username": "string"
    "password": "string"
}
```
### Создать изображение по тексту:
Тело запроса"
```
{
    "prompt": "string",
    "app_id": "string",
    "user_id": "string"
}
```
### Создать изображение по шаблону:
Тело запроса"
```
{
    "template_id": "integer",
    "app_id": "string",
    "user_id": "string"
}
```
### Создать изображение по фото + текст:
Тело запроса"
```
{
    "template_file": "string",
    "app_id": "string",
    "user_id": "string"
}
```
### Создать изображение по фото + шаблон:
Тело запроса"
```
{
    "template_file": "string",
    "template_id": "integer"
    "app_id": "string",
    "user_id": "string"
}
```
## Документация:
Полная документация доступна по адресу:
http://127.0.0.1:8000/swagger/
## Автор:
### Игорь Журавлев
Ссылка на GitHub:
https://github.com/sijey06