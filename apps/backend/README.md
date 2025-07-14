# FoodFleet Backend

Бэкенд для проекта FoodFleet с использованием Domain-Driven Design (DDD) архитектуры.

## Технологический стек

- **Python 3.13+** - язык программирования
- **FastAPI** - веб-фреймворк
- **SQLAlchemy** - ORM для работы с базой данных
- **PostgreSQL** - база данных
- **Pydantic** - валидация данных и сериализация
- **Poetry** - управление зависимостями

## Архитектура

Проект построен по принципам Domain-Driven Design (DDD) со следующей структурой:

- **Domain Layer** - содержит бизнес-логику, сущности и интерфейсы репозиториев
- **Application Layer** - содержит сервисы приложения и DTO
- **Infrastructure Layer** - содержит реализации репозиториев и конфигурацию БД
- **API Layer** - содержит конечные точки API

## Установка и запуск

1. Смена папки:
   ```
   cd foodfleet/apps/backend
   ```

2. Установить зависимости:
   ```
   poetry install
   ```

3. Создать файл .env и настроить переменные окружения:
   ```
   cp .env.example .env
   ```

4. Запустить приложение:
   ```
   poetry run uvicorn app.main:app --reload
   ```

5. Открыть документацию API:
   ```
   http://localhost:8000/docs
   ```

## Пример API

### Ping Endpoint

- **GET /api/v1/ping/** - получить ping ответ
- **POST /api/v1/ping/** - создать новый ping с пользовательским сообщением

## Лицензия

MIT
