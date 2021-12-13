# projet8 - plateforme pour amateurs de Nutella
project openclassrooms P8,
The goal of this web application is to interact with Open Food Facts database to recover the foods,
compare them and offer the user a healthier substitute for the food they want.The user can then save his choice
Application host on Heroku, visible at: [link to github web app](https://purbeurre-forever.herokuapp.com/)


## START
This project uses Python and Requests library. It is advisable to use
a virtual environment to avoid conflicts with other version of libraries.


## pre requirement
to start the webapp, you need:
* Python
* Git
* PostgreSql
* Requests library (auto install later with requirements)


## INSTALLATION

1. Download sources from github repository:
[link to github repo](https://github.com/Jinr0h404/Projet8.git)

You can dowload zip file or dowload with the url and Git:
- create new folder for Project, with Git in root of the folder
- Make git clone https://github.com/Jinr0h404/Projet8.git

1. If you don't have it: Install Python 3.9 and requirements file.
You will find the sources for Python here:
[link to sources](https://www.python.org/downloads/)

1. **Strongly advised:**
Install a virtual environment like Pipenv:
install with command: `pip install pipenv`
to use pipenv: 
in project folder, init virtual env with command: `pipenv shell`
when you are in your virtual environment you can install libraries from requirements
file with command: `pip install -r requirements.txt`


## Application

To start the application
* In the virtual env
* start the web server with command: `python manage.py runserver`


## Result

Server web is running.
You could go on http://127.0.0.1:8000/ to try your app


## PROJECT

made with:

* Django==3.2.9
* gunicorn==20.1.0
* psycopg2==2.9.2
* pytest==6.2.5
* pytest-cov==3.0.0
* pytest-django==4.4.0
* pytest-mock==3.6.1
* requests==2.26.0
* selenium==4.1.0
* whitenoise==5.3.0
* PostgreSql
* bootstrap template from https://startbootstrap.com/ under MIT license
* API Open Food Facts

## Contributor & Author

Ewen Jeannenot & bootstrap template from https://startbootstrap.com/ Copyright (c) 2013-2021 Start Bootstrap LLC