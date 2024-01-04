## Django Web Application Assignment for Cuvette

## Author
Abhinav Kumar

## Overview
This is a simple Django web application that includes user authentication features like user registration (sign up), login, and a basic user profile.

## Features

- User Registration (Sign Up) with fields for username, email, password, and confirm password.
- User Login with fields for username and password.
- Dashboard page displaying a welcome message with the user's username and user information.
- Logout functionality.

## Requirements

- Django 
- Python 

## Setup Instructions

1. Clone the repository:
```
  git clone https://github.com/your-username/your-django-app.git
```
2. Navigate to project directory:
```
  cd your-django-app
```

3. Create a virtual environment(Optional):
```
  python -m venv venv
```
source ```venv/bin/activate```  On Linux/macOS
Or, on Windows: ``` .\venv\Scripts\activate ```

4. Install Django on the running environment. Ignore if already installed globally:
```
  pip install -r requirements.txt
```

5. Make migrations:
```
  python manage.py migrate
```

6. Create a superuser if you want to access Django Admin panel:
```
  python manage.py createsuperuser
```
Then follow the prompts.

7. Run the server:
```
  python manage.py runserver
```

8. Open the application in your web browser: http://127.0.0.1:8000/

## Usage
- Visit the registration page to create a new account.
- Log in using your username and password.
- Access the dashboard page.
- Logout when done.
