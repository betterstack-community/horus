import environ
import pycountry
import requests
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

env = environ.Env()
env.read_env(env.str('ENV_PATH', '.env'))
openweather_api_key = env("OPEN_WEATHER_API_KEY")


def index(request):
    return render(request, 'index.html', {})


def search(request):
    """
    Page showing the results of the location search
    """

    if request.method != 'POST':
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
        return render(request, 'search.html', {'success': False, 'search': location, 'results': f'Unable to find {location}'})

    print(matching_locations.json())

    location_data = [{
        'name': location['name'],
        'lat': location['lat'],
        'lon': location['lon'],
        'country': pycountry.countries.get(alpha_2=location['country']).name,
        'state': location['state'] if 'state' in location else ''
    } for location in matching_locations.json()]

    # TODO: Demonstrate negative example of logging an API key by logging your OpenWeather API key

    return render(request, 'search.html', {'success': True, 'search': location, 'results': location_data})


def weather(request):
    """
    Returns the weather of the searched location
    """
    print(request.POST)

    return render(request, 'weather.html', {})
