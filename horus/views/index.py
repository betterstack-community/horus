import uuid

from django.shortcuts import render


def index(request):
    request.session['id'] = str(uuid.uuid4())
    # TODO: Log when a new user session is created
    return render(request, 'index.html', {})
