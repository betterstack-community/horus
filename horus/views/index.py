import logging
import uuid

from django.shortcuts import render

"""
Start your logging journey here!

We will first create a basic Logger fit with Handlers and Formatters.
"""

# TODO: Create a new logger with name 'horus.views.index'
logger = logging.getLogger('horus.views.index')

# TODO: Create a StreamHandler to output all logs to console
ch = logging.StreamHandler()

# TODO: Set StreamHandler level to include all INFO messages
ch.setLevel(logging.INFO)

# TODO: Create a Formatter that will output the following format: '<name> at <timestamp> (<level>) :: <message>'
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# TODO: Set the above Formatter to the StreamHandler
ch.setFormatter(formatter)

# TODO: Add the StreamHandler to the Logger
logger.addHandler(ch)


def index(request):
    # Assign each request a new UUID to uniquely identify it
    request.session['id'] = str(uuid.uuid4())

    # TODO: Log when a new user session is created
    logger.warning(f'New user with ID: {request.session["id"]}')

    return render(request, 'index.html', {})
