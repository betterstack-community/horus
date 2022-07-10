# Horus

Weather app built on Django

## Introduction

This application aims to demonstrate the fundamentals of logging in Python within the context of a Django application. Thus, the application aims to be as minimal and simplistic as possible to avoid needing to over-explain how Django works which is not the focus.

## Features

- Search location by name
- Get current location weather
- Unique user session tracking

## Setup

```python
git clone https://github.com/woojiahao/horus.git
cd horus/
```

## Local deployment

```python
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Following along

Start your logging journey in `horus/views/index.py` and understand the general steps necessary for setting up a logging system independent of Django using `logging`.

Then, move on to `horus/openweather.py` to use your newly acquired skills to add logging to this file, following the prompts provided.

Once you've gotten comfortable with basic logging skills and conventions, hop over to `horus/views/search.py` for a guided procedure of setting up logging specific to Django.

With that, you can implement your own Django-specific logging in `horus/views/weather.py`.
