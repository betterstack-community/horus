import logging
import uuid

from django.shortcuts import render

"""
Start your logging journey here!

We will first setup a basic logging structure using the default logging features Python provides through the logging
module.

We will do so by creating a Logger and attaching a StreamHandler and Formatter, then we will output when a new user
session is created.
"""

# Create a new logger with name 'horus.views.index'
logger = logging.getLogger('horus.views.index')

# Create a StreamHandler to output all logs to console
ch = logging.StreamHandler()

# Set StreamHandler level to include all INFO messages
ch.setLevel(logging.INFO)

# Create a Formatter that will output the following format: '<name> at <timestamp> (<level>) :: <message>'
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set the above Formatter to the StreamHandler
ch.setFormatter(formatter)

# Add the StreamHandler to the Logger
logger.addHandler(ch)


def index(request):
    # Assign each request a new UUID to uniquely identify it
    request.session['id'] = str(uuid.uuid4())

    # Log when a new user session is created
    logger.warning(f'New user with ID: {request.session["id"]}')

    return render(request, 'index.html', {})
