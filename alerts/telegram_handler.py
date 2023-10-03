import requests

def send_telegram_alert(bot_token, user_id, message):
    base_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": user_id,
        "text": message
    }
    response = requests.post(base_url, data=payload)
    return response.json()
