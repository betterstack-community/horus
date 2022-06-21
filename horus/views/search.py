import logging
from django.shortcuts import redirect, render

from ..openweather import search_countries

"""
Using Django-specific logging configurations

To configure Django-specific logging, modify settings.py with the respective loggers
"""

# Get the logger setup in settings.py
logger = logging.getLogger('horus.views.search')


def search(request):
    # Start logging!

    if request.method != 'POST':
        # Log when invalid access is made
        logger.warning(
            'Invalid access made to /search, page should be accessed through / first')
        return redirect('/')

    # Log the current user when they successfully navigate to this /search page
    logger.info(f'User {request.session["id"]} has navigated to /search')

    location = request.POST['location']

    # Log the location searched
    logger.info(f'User {request.session["id"]} searched for {location}')

    (success, locations) = search_countries(location)

    if not success:
        # Log when the request failed
        logger.warning(f'Failed to find {location} successfully')
        return render(request, 'search.html', {'success': success})

    return render(request, 'search.html', {'success': success, 'search': location, 'results': locations})
