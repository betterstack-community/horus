from django.shortcuts import redirect, render
from openweather import search_countries


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

    (success, locations) = search_countries(location)

    if not success:
        return render(request, 'search.html', {'success': success})

    # TODO: Demonstrate negative example of logging an API key by logging your OpenWeather API key

    return render(request, 'search.html', {'success': success, 'search': location, 'results': locations})
