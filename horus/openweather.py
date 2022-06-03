import environ
import pycountry
import requests

env = environ.Env()
env.read_env(env.str('ENV_PATH', '.env'))
key = env('OPEN_WEATHER_API_KEY')


def __request__(api, params):
    params['appid'] = key
    response = requests.get(api, params)
    return response


def search_countries(search, limit=5):
    response = __request__(
        'http://api.openweathermap.org/geo/1.0/direct',
        {'q': search, 'limit': limit}
    )

    if not response.ok or len(response.json()) == 0:
        return (False, [])

    locations = [{
        'name': location['name'],
        'lat': location['lat'],
        'lon': location['lon'],
        'country': pycountry.countries.get(alpha_2=location['country']).name,
        'state': location['state'] if 'state' in location else ''
    } for location in response.json()]

    return (True, locations)


def get_current_weather(location, lat, lon):
    response = __request__(
        'https://api.openweathermap.org/data/2.5/weather',
        {'lat': lat, 'lon': lon, 'units': 'metric'}
    )

    if not response.ok:
        return (False, {})

    weather = {
        'current': response.json()['weather'][0]['description'].lower(),
        'temp': response.json()['main']['temp'],
        'feels_like': response.json()['main']['feels_like'],
        'location': location
    }

    return (True, weather)
