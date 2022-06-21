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

# Create a new Logger with name 'horus.views.index', this Logger will be used for the entire view
logger = logging.getLogger('horus.views.index')

# Set Logger level to include all INFO and above messages
logger.setLevel(logging.INFO)

# Create a Formatter that will output the following format: '<name> at <timestamp> (<level>) :: <message>'
formatter = logging.Formatter(
    '%(name)s at %(asctime)s (%(levelname)s) :: %(message)s')

# Create a StreamHandler to output all logs to the console
sh = logging.StreamHandler()

# Set the above Formatter to the StreamHandler so that all logs output to the console will follow the given format
sh.setFormatter(formatter)

# Add the StreamHandler to the Logger for the logging to take place
logger.addHandler(sh)


def index(request):
    # Assign each request a new UUID to uniquely identify it
    request.session['id'] = str(uuid.uuid4())

    # Log an information message when a new user accesses the index page
    logger.info(f'New user with ID: {request.session["id"]}')

    return render(request, 'index.html', {})
