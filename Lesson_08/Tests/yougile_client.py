"""Client for Yougile API."""
import requests
from typing import Dict, Any

try:
    from config import BASE_URL, API_KEY, LOGIN, PASSWORD, COMPANY_ID
except ImportError:
    print("❌ Config file not found! Please create config.py from config.example.py")
    raise


class YougileClient:
    """Client for interacting with Yougile API."""

    def __init__(self, base_url: str = BASE_URL):
        """Initialize client."""
        self.base_url = base_url
        self.api_key = API_KEY

    def get_headers(self) -> Dict[str, str]:
        """Get authorization headers."""
        if not self.api_key or self.api_key == "YOUR_API_KEY_HERE":
            raise ValueError(
                "API key not configured. Please set API_KEY in config.py"
            )

        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def create_project(self, title: str) -> Dict[str, Any]:
        """[POST] Create project."""
        data = {"title": title}

        response = requests.post(
            f"{self.base_url}/projects",
            headers=self.get_headers(),
            json=data,
            timeout=10,
        )

        if response.status_code == 201:
            return response.json()
        else:
            error_msg = (
                f"Failed to create project: "
                f"{response.status_code} - {response.text}"
            )
            raise Exception(error_msg)

    def update_project_title(
            self, project_id: str, new_title: str
    ) -> Dict[str, Any]:
        """[PUT] Update project title."""
        data = {"title": new_title}

        response = requests.put(
            f"{self.base_url}/projects/{project_id}",
            headers=self.get_headers(),
            json=data,
            timeout=10,
        )

        if response.status_code == 200:
            return response.json()
        else:
            error_msg = (
                f"Failed to update project: "
                f"{response.status_code} - {response.text}"
            )
            raise Exception(error_msg)

    def get_project(self, project_id: str) -> Dict[str, Any]:
        """[GET] Get project by ID."""
        response = requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.get_headers(),
            timeout=10,
        )

        if response.status_code == 200:
            return response.json()
        else:
            error_msg = (
                f"Failed to get project: "
                f"{response.status_code} - {response.text}"
            )
            raise Exception(error_msg)

    def delete_project(self, project_id: str) -> bool:
        """Delete project (for cleanup)."""
        response = requests.delete(
            f"{self.base_url}/projects/{project_id}",
            headers=self.get_headers(),
            timeout=10,
        )

        return response.status_code in [204, 404]


def get_api_key():
    """Get new API key using credentials from config."""
    auth_data = {
        "login": LOGIN,
        "password": PASSWORD,
        "companyId": COMPANY_ID,
    }

    print("Получаем API ключ...")

    try:
        response = requests.post(
            f"{BASE_URL}/auth/keys",
            json=auth_data,
            headers={"Content-Type": "application/json"},
            timeout=10,
        )

        print(f"Статус: {response.status_code}")
        print(f"Ответ: {response.text}")

        if response.status_code == 201:
            data = response.json()
            api_key = data.get("key")
            print("✅ Новый API ключ получен!")
            print(f"🔑 Ключ: {api_key}")
            return api_key
        else:
            print("❌ Не удалось получить API ключ")
            return None

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return None