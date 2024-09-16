# GitHub API Test

Этот проект содержит автоматический тест для проверки работы с GitHub API. Тест создает новый публичный репозиторий, проверяет его наличие в списке репозиториев пользователя, а затем удаляет его.

## 🛠 Требования

- Python 3.10+
- pip (менеджер пакетов Python)
- GitHub аккаунт
- Персональный токен доступа GitHub с правами на создание и удаление репозиториев

## 📦 Установка

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/inspectorrrrr/github-api-test.git
   cd github-api-test
   ```

2. Создайте и активируйте виртуальное окружение (рекомендуется):
   ```
   python -m venv venv
   source venv/bin/activate  # Для Unix или MacOS
   venv\Scripts\activate  # Для Windows
   ```

3. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

## ⚙️ Настройка

1. Отредактируйте файл `.env`, заполнив следующие переменные:
   - `GITHUB_TOKEN`: ваш персональный токен доступа GitHub
   - `GITHUB_USERNAME`: ваше имя пользователя на GitHub
   - `REPO_NAME`: имя тестового репозитория (например, "test-qweasdzxc")

## 🚀 Запуск теста

Для запуска теста выполните следующую команду:

```
python test_api.py
```

## 📝 Структура проекта

- `test_api.py`: основной скрипт с тестом
- `.env`: файл с переменными окружения
- `requirements.txt`: файл с зависимостями
- `README.md`: инструкция по установке и запуску
