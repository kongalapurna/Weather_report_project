import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print('\n** Get current weather conditions **\n')
    city = input('\nPlease enter city name:\n')
    
    requests_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"
    
    weather = requests.get(requests_url).json()
    print(f"\nCurrent weather for: {weather['name']}")
    print(f"The Temp is:  {weather['main']['temp']}")
    print(f"Feels like {weather['main']['feels_like']} and {weather['weather'][0]['description']}")
#     pprint(weather)


get_current_weather()