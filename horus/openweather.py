import environ
import pycountry
import requests

"""
Practice setting up Django-independent logging here!

Like in index.py, we will setup a basic logging structure, but this time, create a handler to save all warnings to a
file while logging all messages to the console as per usual.

To improve the usefulness of the log messages, follow these three simple steps:
1. Be as specific as possible about the site of the log
2. Use appropriate log levels that correspond to the respective severities of the events
3. Include as much information about the log, instead of just printing results
"""

env = environ.Env()
env.read_env(env.str('ENV_PATH', '.env'))


class OpenWeatherError(Exception):
    """Raised when an error occurs with calling the OpenWeather API"""
    pass


# TODO: Create a new Logger with name 'horus.openweather'

# TODO: Set the Logger level to include all INFO and above messages

# TODO: Create a Formatter that will output the following format: '<name> at <timestamp> (level) :: <message>'

# TODO: Create a StreamHandler to output all logs to the console

# TODO: Create a FileHandler to save all WARNING and above logs to a file (hint: set the log level of the FileHandler)

# TODO: Set the above Formatter to both the StreamHandler and FileHandler

# TODO: Add both the StreamHandler and FileHandler to the Logger

# TODO: Demonstrate a bad example of logging by logging the API key to the console
key = env('OPEN_WEATHER_API_KEY')


def __request__(api, params):
    params['appid'] = key
    response = requests.get(api, params)
    return response


def search_countries(search, limit=5):
    # TODO: Log the search submitted

    # TODO: Log the results of the API request
    response = __request__(
        'http://api.openweathermap.org/geo/1.0/direct',
        {'q': search, 'limit': limit}
    )

    if not response.ok or len(response.json()) == 0:
        # TODO: Log when the returned values are invalid
        raise OpenWeatherError(
            'OpenWeather could not find matching locations - response not OK or response is empty')

    # TODO: Log the parsed locations
    locations = [{
        'name': location['name'],
        'lat': location['lat'],
        'lon': location['lon'],
        'country': pycountry.countries.get(alpha_2=location['country']).name,
        'state': location['state'] if 'state' in location else ''
    } for location in response.json()]

    return locations


def get_current_weather(location, lat, lon):
    # TODO: Log the arguments of this function

    # TODO: Log the results of the API request
    response = __request__(
        'https://api.openweathermap.org/data/2.5/weather',
        {'lat': lat, 'lon': lon, 'units': 'metric'}
    )

    if not response.ok:
        # TODO: Log when the API request fails
        raise OpenWeatherError(
            'OpenWeather could not find the weather of the location - response not OK')

    # TODO: Log the parsed weather
    weather = {
        'current': response.json()['weather'][0]['description'].lower(),
        'temp': response.json()['main']['temp'],
        'feels_like': response.json()['main']['feels_like'],
        'location': location
    }

    return weather
