# Cars Dealership Application

## Project Description
A full-stack Cars Dealership application that allows users to explore car dealerships, view dealer details, register and log in, and submit dealership reviews.

## Technologies Used
- **Frontend:** React, HTML, CSS, JavaScript
- **Backend:** Python, Django, Django REST Framework
- **Database:** SQLite
- **API Testing:** cURL
- **Version Control:** Git and GitHub

## Features
- User registration and login
- User authentication and logout
- View all car dealerships
- Search and filter dealerships by state
- View dealership details
- Read and submit dealership reviews
- Sentiment analysis of customer reviews
- Display car makes and models
- About and Contact pages

## Project Structure
```text
cars-dealership/
├── server/
│   ├── dealers/
│   ├── djangoproj/
│   ├── frontend/
│   └── manage.py
├── README.md
└── .gitignore
```

## How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/cars-dealership.git
cd cars-dealership
```

### 2. Set Up the Backend
```bash
cd server
python -m venv venv
```

Activate the virtual environment on Windows:
```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:
```bash
pip install django djangorestframework django-cors-headers
```

### 3. Run Database Migrations
```bash
python manage.py migrate
```

### 4. Start the Django Server
```bash
python manage.py runserver
```

Open the application at:
`http://127.0.0.1:8000/`

### 5. Run the Frontend
Open another terminal:
```bash
cd server/frontend
npm install
npm run dev
```

## API Endpoints
- `GET /api/dealers/` – Retrieve all dealerships
- `GET /api/dealer/<dealer_id>/` – Retrieve dealership details
- `GET /api/dealers/state/<state>/` – Filter dealerships by state
- `GET /api/dealer/<dealer_id>/reviews/` – Retrieve dealership reviews
- `POST /api/dealer/<dealer_id>/reviews/submit/` – Submit a dealership review
- `POST /api/register/` – Register a user
- `POST
