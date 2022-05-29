# Horus

Weather app built on Django

## Introduction

This application aims to demonstrate the fundamentals of logging in Python within the context of a Django application. Thus, the application aims to be as minimal and simplistic as possible to avoid needing to over-explain how Django works which is not the focus.

## Features

- Search location by name
- Get current location weather
- Unique user session tracking (demonstrated using Heroku)

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
