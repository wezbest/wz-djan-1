
1. [r3](#r3)


# r3 

1. Third attempt at installing and running django
2. This is where you will start following thet tutorial 

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
3. Acording to the tutorial the above is just to setup the django application , then within that you careate apps

Command to start an app inside django 
```py 
uv run manage.py startapp p1
```