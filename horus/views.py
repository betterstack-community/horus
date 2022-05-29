import uuid

import environ
import pycountry
import requests
from django.shortcuts import redirect, render

# TODO: Enable logging with requests library

env = environ.Env()
env.read_env(env.str('ENV_PATH', '.env'))
openweather_api_key = env("OPEN_WEATHER_API_KEY")


def index(request):
    request.session['id'] = str(uuid.uuid4())
    # TODO: Log when a new user session is created
    return render(request, 'index.html', {})


def search(request):
    """
    Page showing the results of the location search
    """

    if request.method != 'POST':
        # TODO: Log when invalid access is made
        return redirect('/')

    # TODO: Log when user navigates to search page successfully

    location = request.POST['location']

    # TODO: Add logging for the location searched

    # TODO: Log the locations found from the API request
    api = 'http://api.openweathermap.org/geo/1.0/direct'
    response = requests.get(
        api,
        params={
            'q': location,
            'appid': openweather_api_key,
            'limit': 5
        })

    if not response.ok or len(response.json()) == 0:
        # TODO: Log when the returned values are invalid
        return render(request, 'search.html', {'success': False, 'search': location, 'results': f'Unable to find {location}'})

    locations = [{
        'name': location['name'],
        'lat': location['lat'],
        'lon': location['lon'],
        'country': pycountry.countries.get(alpha_2=location['country']).name,
        'state': location['state'] if 'state' in location else '',
    } for location in response.json()]

    # TODO: Demonstrate negative example of logging an API key by logging your OpenWeather API key

    return render(request, 'search.html', {'success': True, 'search': location, 'results': locations})


def weather(request):
    """
    Page showing the weather information from the selected location
    """

    if request.method != 'POST':
        # TODO: Log when invalid access is made
        return redirect('/')

    # TODO: Log when user navigates to weather page successfully

    # TODO: Log the POST body

    # TODO: Log the latitude and longitude
    input = request.POST['location'].split(', ')

    api = 'https://api.openweathermap.org/data/2.5/weather'
    response = requests.get(
        api,
        params={
            'lat': float(input[1]),
            'lon': float(input[2]),
            'appid': openweather_api_key,
            'units': 'metric'
        })

    # TODO: Log response from API

    if not response.ok:
        # TODO: Log when request failed
        return render(request, 'weather.html', {'success': False, 'weather': f'Invalid location selected...'})

    weather = {
        'current': response.json()['weather'][0]['description'].lower(),
        'temp': response.json()['main']['temp'],
        'feels_like': response.json()['main']['feels_like'],
        'location': input[0]
    }
    return render(request, 'weather.html', {'success': True, 'weather': weather})
