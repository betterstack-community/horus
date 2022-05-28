import environ
import pycountry
import requests
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
import uuid

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
    print(request.session['id'])

    if request.method != 'POST':
        # TODO: Log when invalid access it made
        return redirect('/')

    location = request.POST['location']

    # TODO: Add logging for the location searched

    # TODO: Log the locations found from the API request
    # TODO: Enable logging with requests library
    geocoding_api_base = 'http://api.openweathermap.org/geo/1.0/direct'
    matching_locations = requests.get(
        geocoding_api_base,
        params={
            'q': location,
            'appid': openweather_api_key,
            'limit': 5
        })

    if not matching_locations.ok or len(matching_locations.json()) == 0:
        # TODO: Log when the returned values are invalid
        return render(request, 'search.html', {'success': False, 'search': location, 'results': f'Unable to find {location}'})

    print(matching_locations.json())

    location_data = [{
        'name': location['name'],
        'lat': location['lat'],
        'lon': location['lon'],
        'country': pycountry.countries.get(alpha_2=location['country']).name,
        'state': location['state'] if 'state' in location else '',
    } for location in matching_locations.json()]

    # TODO: Demonstrate negative example of logging an API key by logging your OpenWeather API key

    return render(request, 'search.html', {'success': True, 'search': location, 'results': location_data})


def weather(request):
    """
    Page showing the weather information from the selected location
    """
    if request.method != 'POST':
        return redirect('/')

    # TODO: Log the POST body
    print(request.POST)

    # TODO: Log the latitude and longitude
    input = request.POST['location'].split(', ')

    # TODO: Log the API request made
    weather_api_base = 'https://api.openweathermap.org/data/2.5/weather'
    api_response = requests.get(
        weather_api_base,
        params={
            'lat': float(input[1]),
            'lon': float(input[2]),
            'appid': openweather_api_key,
            'units': 'metric'
        })

    print(api_response.json())

    if not api_response.ok:
        return render(request, 'weather.html', {'success': False, 'weather': f'Invalid location selected...'})

    weather = {
        'current': api_response.json()['weather'][0]['description'].lower(),
        'temp': api_response.json()['main']['temp'],
        'feels_like': api_response.json()['main']['feels_like'],
        'location': input[0]
    }
    return render(request, 'weather.html', {'success': True, 'weather': weather})
