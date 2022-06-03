import uuid

import environ
import pycountry
import requests
from django.shortcuts import redirect, render


env = environ.Env()
env.read_env(env.str('ENV_PATH', '.env'))
openweather_api_key = env("OPEN_WEATHER_API_KEY")




