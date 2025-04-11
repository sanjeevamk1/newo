import requests
import time
from plyer import notification
import winsound

url = "https://rcbmpapi.ticketgenie.in/ticket/eventlist/O"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-IN,en;q=0.9,kn-IN;q=0.8,kn;q=0.7,en-GB;q=0.6,en-US;q=0.5,te;q=0.4",
    "origin": "https://shop.royalchallengers.com",
    "referer": "https://shop.royalchallengers.com/ticket",
    "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

def beep():
    duration = 1000  
    freq = 750  
    winsound.Beep(freq, duration)

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

def send_telegram(message):
    token = "Yourtoken"
    chat_id = "yourchatid"  # Make sure this is correct
    telegram_url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    response = requests.post(telegram_url, data=data)
    print("Telegram Status:", response.status_code)
    print("Telegram Response:", response.json())

while True:
    try:
        print("Checking for CSK tickets...")
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            for each in data.get('result', []):
                if each.get('team_2') == "Chennai Super Kings":
                    print("Tickets are live for CSK match!")
                    send_notification("CSK Match Alert", "Tickets are live for Chennai Super Kings!")
                    beep()
                    send_telegram("Tickets are LIVE for CSK match!")
                    break
                else:
                    print("Still waiting...")

        else:
            print("Failed to fetch data. Status code:", response.status_code)
    
    except Exception as e:
        print("Error:", e)

    time.sleep(900) 