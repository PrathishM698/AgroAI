import requests

API_KEY = "f7a36cb27ba5dbc62e38bb853a020809"

def get_weather(city="Chennai"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    # DEBUG: see what API returns
    print("API RESPONSE:", data)

    # SAFE CHECK (prevents crash)
    if "main" not in data:
        return {
            "temperature": "Not Available",
            "humidity": "Not Available"
        }

    return {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"]
    }