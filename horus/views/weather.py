import uuid

import environ
import pycountry
import requests
from django.shortcuts import redirect, render

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
