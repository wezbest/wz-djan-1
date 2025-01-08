
1. [Proj1](#proj1)
2. [Commands Used](#commands-used)
   1. [Step to start a django project with uv](#step-to-start-a-django-project-with-uv)
   2. [Creating a app](#creating-a-app)
   3. [Creating Migrations](#creating-migrations)


# Proj1 

Actual Project from tutorial being done here

1. Third attempt at installing and running django
2. This is where you will start following thet tutorial 
3. The way django works is by creating a project and then apps inside it

# Commands Used 

## Step to start a django project with uv 

```sh 
# Set up a new uv project 
uv init p1

# Go inside the project and run it th first time to create the venv
uv run hello.py

# Then add the django and any other py pkg 
uv add rich django 

# Test if django is installed 
uv run django-admin --version

# Setup a new djano project - note you need to make a dir first 
uv run django-admin startproject p1

# Run the project - This will open the project in localhost
uv run python manage.py runserver
```

1. Note since you have an empty project you can just use the intial entry point python file for printing instructions
2. You can use the rich library which can rener markdown directly on screen

## Creating a app

```py 
uv run manage.py startapp app1
```
- This is also menioned in the official docs

## Creating Migrations 

1. After creating the db schema in `app/models.py`

```sh 
uv run manage.py makemigrations 
```