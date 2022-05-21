from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    return render(request, 'index.html', {})


def search(request):
    """
    Returns the search results of the initial location search
    """

    if request.method == 'POST':
        # TODO: Add logging for the location searched

        results = ['Hello', 'Pineapple']

        return render(request, 'search.html', {'search': request.POST['location'], 'results': results})
    else:
        return render(request, 'index.html', {})


def weather(request):
    """
    Returns the weather of the searched location
    """
    # return render(request, )
    pass
