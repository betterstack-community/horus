from django.shortcuts import redirect, render

from ..openweather import get_current_weather

"""
Practice using Django-specific logging here!

Like in settings.py and search.py, we will first setup the basic logging details in settings.py before retrieving the
configured logger here.
"""

# TODO: Get logger 'horus.views.weather' setup in settings.py


def weather(request):
    if request.method != 'POST':
        # TODO: Log when invalid access is made
        return redirect('/')

    # TODO: Log when user navigates to weather page successfully

    # TODO: Log the POST body

    # TODO: Log the latitude and longitude
    input = request.POST['location'].split(', ')

    (success, weather) = get_current_weather(
        input[0], float(input[1]), float(input[2]))

    if not success:
        # TODO: Log when request failed
        return render(request, 'weather.html', {'success': success})

    return render(request, 'weather.html', {'success': success, 'weather': weather})
