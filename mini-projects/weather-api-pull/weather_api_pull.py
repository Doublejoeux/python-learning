#Weather-API pull
import requests
city = input("Enter City name: ").title()
try:
    response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1", timeout= 30)
    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])
        if len(results) > 0:
            if city in results[0]["name"]:
                lat = results[0].get("latitude", "N/A")
                lon = results[0].get("longitude", "N/A")
            else:
                 print("N/A")
                 exit()
        else:
            print("Invalid")
            exit()         
    else:
        print(f"Something Went Wrong: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Something Went Wrong: {e}")
    exit()

try:
    response2 = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true", timeout= 30)
    if response2.status_code == 200:
        data2 = response2.json()
        print (data2)
        temp = data2.get("current_weather", {}).get("temperature", "N/A")
        temp_unit = data2.get("current_weather_units", {}).get("temperature", "N/A")
        windspeed = data2.get("current_weather", {}).get("windspeed", "N/A")
        windspeed_unit = data2.get("current_weather_units", {}).get("windspeed", "N/A")
        weathercode = data2.get("current_weather", {}).get("weathercode", "N/A")
    else:
        print(f"Something Went Wrong: {response2.status_code}")
        exit()
except requests.exceptions.RequestException as d:
    print(f"Something Went Wrong: {d}")
    exit()

weathercodes = {
    0: "Clear Sky",
    1: "Mainly clear", 
    2: "partly cloudy",
    3: "overcast",
    45: "Fog",
    48: "depositing rime fog",
    51: "Light Drizzle",
    53: "Moderate Drizzle",
    55: "Dense Intensity Drizzle",
    56: "Light Freezing Drizzle",
    57: "Dense Intensity Freezing Drizzle",
    61: "Slight Rain",
    63: "Moderate Rain",
    65: "Heavy Intensity Rain",
    66: "Light Freezing Rain",
    67: "Heavy Intensity Freezing Rain",
    71: "Slight Snowfall",
    73: "Moderate Snowfall",
    75: "Heavy Intensity Snowfall",
    77: "Snow grains",
    80: "Slight Rain Showers",
    81: "Moderate Rain Showers",
    82: "Violent Rain Showers",
    85: "Slight Snow Showers",
    86: "Heavy Snow Showers",
    95: "Slight or Moderate Thunderstorm",
    96: "Slight Thunderstorm",
    99: "Heavy Hail Thunderstorm"
    }

def get_weathercode():
        print(weathercodes[weathercode])

print(f"City name: {city}")
print(f"Temperature: {temp}{temp_unit}")
print(f"Windspeed: {windspeed}{windspeed_unit}")
get_weathercode()