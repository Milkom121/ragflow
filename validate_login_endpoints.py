import requests

BASE_URL = "http://localhost"  # Modifica se il backend gira su una porta diversa

def test_login():
    url = f"{BASE_URL}/v1/user/login"
    payload = {
        "username": "mariomattiadimuro@gmail.com",  # Sostituisci con utente valido
        "password": "Ghosts121!"  # Sostituisci con password valida
    }
    try:
        response = requests.post(url, json=payload)
        print(f"Test /v1/user/login: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Errore chiamata /v1/user/login: {e}")

def test_login_channels():
    url = f"{BASE_URL}/v1/user/login/channels"
    try:
        response = requests.get(url)
        print(f"Test /v1/user/login/channels: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Errore chiamata /v1/user/login/channels: {e}")

if __name__ == "__main__":
    print("=== Validazione rapida endpoint login ===")
    test_login()
    test_login_channels()
