from django.shortcuts import redirect, render


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
