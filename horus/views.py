from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    return render(request, 'index.html', {})


def search(request):
    """
    Returns the search results of the initial location search
    """
    # TODO: Add logging for the location searched
    print(request)
    return render(request, 'index.html', {'d': 'hi'})


def weather(request):
    """
    Returns the weather of the searched location
    """
    return render(request, )
