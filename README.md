# Gerbil Django Pet Project
### This project was created to dig dipper into the Django framework. Main idea is to create Gerbils, their houses and cages. The pages reflect information about every Gerbil, House and Cage.

## To launch the project:
1. Clone the repo to the preferable place on your device by running:

`$ git clone git@github.com:norka2233/gerbil_django_project.git`

2. Open the project in the preferable IDE.
3. Create virtual environment by running:

`$ python3 -m venv venv`

`source venv/bin/activate`
4. Install all needed packages by running:

`(venv) pip install -r requirements.txt`
5. Create and run a database:

`(venv) python3 manage.py makemigrations gerbil_animal`

`(venv) python3 manage.py makemigrations gerbil_house`

`(venv) python3 manage.py makemigrations gerbil_cage`

`(venv) python3 manage.py migrate`
6.Run the project:

`python3 manage.py runserver`
7. Open 'http://127.0.0.1:8000/gerbil/' in your browser
8. Enjoy the app.