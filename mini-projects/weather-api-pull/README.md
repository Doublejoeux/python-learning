# Weather API Pull

A CLI of a weather app that pulls details of the weather conditions of
specific cities by name from a free online weather API and displays the
city name, temperature, windspeed and weathercode.

## Features
- Searches for the city by name provided by user.
- Displays city name, temperature, windspeed and weathercode if the city
exists and is found.
- Handles situations where the city doesn't exist or not found instead of
crashing.

## How It Works
- Made the search of cities by name possible by using `requests.get()`
to pull the latitude and longitude of the city from the API of 
`https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1`.
- Once the latitude and longitude is gotten, `requests.get()` is used again
to get the temperature, windspeed and weathercode from the API of
`https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true`
using the latitude and longitude of the chosen city.
- `try/except` were used before `requests.get()` to handle `requests.exceptions.RequestException`
errors to prevent the program from crashing.
- `get_weathercode()` displays the `weathercode` from the dictionary `weathercodes` gotten from open-meteo
website docs using the `weathercode` pulled from the API.
- `exit()` is used on all failure paths for the invalid inputs to stop the program from running in a bad state
and catching errors.

## What I Learned
- Encountered an attribute error when I chained into `data` to get the `lat` which is the latitude
of the city. It helped me to strengthen my knowledge on chaining into APIs which doesn't allow the use
of `.get()` on lists.
- Ran into an Index Error when trying to validate if the `city` input exists or is found and figured I
had the code backwards. I was indexing into `'results[0]'`before checking if it was empty with `if len(results) > 0:`.
Switched both codes to check if `'results'` was empty before indexing into it.
- Initially used a lot of `try/except` to handle a lot of Name Errors popping up downstream the code that stemmed
from subsequent failure paths that didn't stop. Used `exit()` to stop the program running after a failure
path to fix it and got rid of the excess `try/except`
- Used `try/except` to handle the `requests.exceptions.RequestException` errors which would occur if `response` didn't get to run and handled checking `response.status_code` using `if/else` which could give an error if `response` ran but an error
occured.

## How to Run It
```bash
python weather_api_pull.py
```
use `pip install requests` in terminal to install the `requests` library if not already pre-installed.

## Possible Improvement
- Showing the weather conditions forecast for each hour across the day and possibly beyond.
