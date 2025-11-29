"""Get API key for Yougile."""
import requests


def get_api_key():
    """Get new API key."""
    base_url = "https://ru.yougile.com/api-v2"

    auth_data = {
        "login": "gushin615542@ya.ru",
        "password": "WocsXY8FTU",
        "companyId": "0081d8d4-c202-4730-af3f-5409d95a02e6",
    }

    print("Получаем API ключ...")

    try:
        response = requests.post(
            f"{base_url}/auth/keys",
            json=auth_data,
            headers={"Content-Type": "application/json"},
            timeout=10,
        )

        print(f"Статус: {response.status_code}")
        print(f"Ответ: {response.text}")

        # Yougile возвращает 201 при успешном создании ключа
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


if __name__ == "__main__":
    api_key = get_api_key()
    if api_key:
        print("\n🎉 Используйте этот ключ в тестах!")
