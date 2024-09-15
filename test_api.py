import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получаем данные из переменных окружения
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
REPO_NAME = os.getenv("REPO_NAME")

# Базовый URL GitHub API
BASE_URL = "https://api.github.com"

# Заголовки для аутентификации
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}


def create_repository(repo_name):
    """Создание нового репозитория"""
    url = f"{BASE_URL}/user/repos"
    payload = {"name": repo_name, "auto_init": True, "private": False}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        print(f"✅ Репозиторий '{repo_name}' успешно создан.")
    else:
        print(f"❌ Ошибка при создании репозитория: {response.status_code}, {response.json()}")


def list_repositories():
    """Получение списка репозиториев пользователя"""
    url = f"{BASE_URL}/user/repos"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repos = response.json()
        repo_names = [repo["name"] for repo in repos]
        print("Список репозиториев:")
        for name in repo_names:
            print(f"- {name}")
        return repo_names
    else:
        print(f"❌ Ошибка при получении списка репозиториев: {response.status_code}, {response.json()}")
        return []


def delete_repository(repo_name):
    """Удаление репозитория"""
    url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{repo_name}"

    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f"✅ Репозиторий '{repo_name}' успешно удалён.")
    else:
        print(f"❌ Ошибка при удалении репозитория: {response.status_code}, {response.json()}")


def main():
    # Шаг 1: Создание нового репозитория
    create_repository(REPO_NAME)

    # Шаг 2: Проверка, что репозиторий был создан
    repos = list_repositories()
    if REPO_NAME in repos:
        print(f"✅ Репозиторий '{REPO_NAME}' найден в списке.")
    else:
        print(f"❌ Репозиторий '{REPO_NAME}' не найден.")

    # Шаг 3: Удаление репозитория
    delete_repository(REPO_NAME)


if __name__ == "__main__":
    main()
