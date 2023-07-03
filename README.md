# Horus

A simple weather app built with Django. This application serves to demonstrate
the fundamentals of logging in Python within the context of a Django
application.

**See the full tutorial**:
[How to Get Started with Logging in Django](https://betterstack.com/community/guides/logging/how-to-start-logging-with-django/).

## 🟢 Prerequisites

- [Python 3.10](https://docs.python.org/3/using/index.html) or later.
- [SQLite](https://www.servermania.com/kb/articles/install-sqlite/).

## 📦 Getting started

- Clone the GitHub repository and `cd` into it:

```bash
git clone https://github.com/woojiahao/horus.git && cd horus
```

- Install all application dependencies:

```bash
pip install -r requirements.txt
```

- Run the database migrations

```bash
python manage.py migrate
```

- Sign up for a [free OpenWeatherMap account](https://openweathermap.org/) and
  retrieve your API key.

- Create a `.env` file at the root of your project with the following contents:

```text
OPEN_WEATHER_API_KEY=<api key>
```

- Start the development server at localhost:8000:

```bash
python manage.py runserver
```

- View the application in your browser, and
  [follow the tutorial](https://betterstack.com/community/guides/logging/how-to-start-logging-with-django/)
  to learn more.

## ⚖ License

The code used in this project and in the linked tutorial are licensed under the
[Apache License, Version 2.0](LICENSE).
