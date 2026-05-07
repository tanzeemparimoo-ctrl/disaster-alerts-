
import requests
from datetime import datetime

API_KEY = 32b3e88f0de62e39683954992c801b82

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("cod") != 200:
            print("\n❌ City not found or API error.")
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        print("\n" + "="*40)
        print(f"🌍 Weather Report for {city.upper()}")
        print("="*40)
        print(f"⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬️ Wind Speed: {wind} m/s")
        print(f"☁️ Condition: {weather}")
        print("="*40)

        # Smart risk logic (upgraded)
        risk_score = 0

        if "rain" in weather or "storm" in weather:
            risk_score += 2
        if temp < 5 or temp > 40:
            risk_score += 2
        if humidity > 80:
            risk_score += 1
        if wind > 10:
            risk_score += 1

        print("\n🚨 DISASTER ALERT STATUS:")

        if risk_score >= 4:
            print("🔴 HIGH RISK - Avoid travel. Stay indoors.")
        elif risk_score == 3:
            print("🟡 MEDIUM RISK - Be cautious if going बाहर.")
        else:
            print("🟢 LOW RISK - Normal weather conditions.")

        print("="*40)

    except requests.exceptions.RequestException:
        print("\n❌ Network error. Check internet connection.")

# Run app
city = input("Enter city name: ")
get_weather(city)
