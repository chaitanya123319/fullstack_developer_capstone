# Best Cars Dealership

**Repository name:** `fullstack_developer_capstone`
**Project name:** Best Cars Dealership

A full-stack web application for finding car dealerships, reading customer reviews and posting your own.
Built as the capstone project for the IBM Full Stack Developer course.

## Features

- Browse 50 dealerships and filter them by state
- View a dealer's details and customer reviews
- Sentiment analysis on every review (positive, neutral or negative)
- Register, log in and log out
- Logged-in users can post a review for a dealer
- About Us and Contact Us pages
- Django admin for managing car makes and models

## Architecture

| Service | Technology | Port |
|---|---|---|
| Web app and user API | Django + React | 8000 |
| Dealers and reviews API | Express + MongoDB | 3030 |
| Sentiment analyzer | Flask + NLTK VADER | 5050 |

## Project structure

```
server/
  djangoproj/            Django project settings and root URLs
  djangoapp/             Auth, car makes/models, proxy views, admin
    microservices/       Sentiment analyzer (Flask)
  database/              Express + MongoDB API, sample data, docker-compose
  frontend/
    static/              About.html, Contact.html, style.css
    src/                 React components (Register, Login, Dealers, Dealer, PostReview)
.github/workflows/       CI: Python (flake8) and JavaScript (JSHint) lint jobs
```

## Run locally

1. **Dealers and reviews API** (needs Docker)
   ```
   cd server/database
   docker compose up --build
   ```
2. **Sentiment analyzer**
   ```
   cd server/djangoapp/microservices
   pip install -r requirements.txt
   python app.py
   ```
3. **Django app**
   ```
   cd server
   pip install -r requirements.txt
   python manage.py makemigrations djangoapp
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

Environment variables (see `server/.env.example`): `backend_url` and `sentiment_analyzer_url`.

## API endpoints

Django (port 8000)

| Method | Path | Purpose |
|---|---|---|
| POST | `/djangoapp/login` | Log in with `{"userName", "password"}` |
| GET | `/djangoapp/logout` | Log out |
| POST | `/djangoapp/register` | Create an account |
| GET | `/djangoapp/get_cars` | All car makes and models |
| GET | `/djangoapp/get_dealers[/<state>]` | Dealers, optionally by state |
| GET | `/djangoapp/dealer/<id>` | One dealer |
| GET | `/djangoapp/reviews/dealer/<id>` | Reviews for a dealer, with sentiment |
| POST | `/djangoapp/add_review` | Post a review (login required) |

Express (port 3030): `/fetchDealers`, `/fetchDealers/<state>`, `/fetchDealer/<id>`,
`/fetchReviews`, `/fetchReviews/dealer/<id>`, `POST /insert_review`.

Sentiment analyzer (port 5050): `GET /analyze/<text>` returns `{"sentiment": "positive"}`.

## Sample data

`server/database/data/` holds 50 sample dealers and their reviews. They are made-up demo data.
Regenerate them with `python server/database/generate_data.py`.

## Continuous integration

`.github/workflows/main.yml` runs two jobs on every push and pull request:
**Lint Python files** (flake8) and **Lint JavaScript files** (JSHint).
