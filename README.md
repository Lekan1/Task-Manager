# Task Management Application

A simple task management application built with Django, implementing user authentication and AJAX for task management.

## Features

- User registration and authentication
- Create, update, delete, and view tasks
- Mark tasks as completed or not completed
- AJAX integration for smooth task management
- MySQL as the database backend

## Requirements

- Python 3.10+
- Django 5.0.6
- MySQL

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/taskmanager.git
   cd taskmanager


2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3.Install the required packages:

pip install -r requirements.txt


4.Configure the database settings:
Open taskmanager/settings.py and configure the DATABASES setting with your MySQL credentials.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'taskmanager',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5.Apply migrations:
python manage.py makemigrations tasks
python manage.py migrate


6.Create a superuser:

python manage.py createsuperuser

7.Run the development server:

python manage.py runserver

8.Access the application:

Open your web browser and go to http://127.0.0.1:8000/.


Usage
Register a new user:

Go to http://127.0.0.1:8000/register/ to create a new account.

Login:

Go to http://127.0.0.1:8000/accounts/login/ to log in.

Manage Tasks:

After logging in, you can create, update, delete, and view your tasks on the main page.

Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.


### Instructions:

1. Replace placeholders like `yourusername`, `your_mysql_username`, and `your_mysql_password` with actual values.
2. Add a `requirements.txt` file listing the dependencies:

   ```txt
   Django==5.0.6
   mysqlclient

