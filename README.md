# Cyber Security Base 2023 - Insecure Website

## Installation instructions

1. After cloning the repository, install the Python packages in requirements.txt (preferable in a virtual environment):

```
pip install -r requirements.txt
```

2. Create the migrations and use them to create the website database file:

```
py manage.py makemigrations
py manage.py migrate
```

3. Create an admin user and follow the instructions:

```
py manage.py createsuperuser
```

4. Start the web server:

```
py manage.py runserver
```

5. Login as admin on the web server at http://localhost:8000/admin. Create additional Users and an Account that is associated with each User.
