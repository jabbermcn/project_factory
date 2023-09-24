# Используйте официальный образ Python с вашей предпочитаемой версией Python
FROM python:3.11

# Установите рабочую директорию в контейнере
WORKDIR /project_factory

# Установите переменные окружения для Django
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Скопируйте зависимости проекта в рабочую директорию
COPY requirements.txt ./

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте остальные файлы проекта в рабочую директорию
COPY . .

# Запустите Django сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
