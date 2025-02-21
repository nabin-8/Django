# Django
## What is Django?

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It is designed to help developers take applications from concept to completion as quickly as possible.

## Why Should You Use Django?

- **Fast Development**: Django's built-in features and tools allow for rapid development.
- **Secure**: Django takes security seriously and helps developers avoid many common security mistakes.
- **Scalable**: Django can handle the heaviest traffic demands.
- **Versatile**: Django is used for all kinds of web applications, from content management systems to social networks.

## Software Installation

### Code Editor

You can use any code editor, but some popular choices are:
- Visual Studio Code
- PyCharm
- Sublime Text

### Python Interpreter

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

## Creating and Activating a Virtual Environment

1. **Install `virtualenv`**:
    ```bash
    pip install virtualenv
    ```

2. **Create a Virtual Environment**:
    ```bash
    virtualenv venv
    ```
    #### OR USING PIP
    ```bash
    Ubuntu
    apt install python3-venv

    mac/windows
    pip3 install pipenv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

Once activated, your terminal prompt will change to indicate that you are working inside the virtual environment.

## Creating Your First Django Project

### Step 1: Create a Virtual Environment

Refer to the previous section on creating and activating a virtual environment.

### Step 2: Activate and Deactivate the Virtual Environment

To activate the virtual environment, use the following commands:

- On Windows:
    ```bash
    venv\Scripts\activate
    ```
- On macOS and Linux:
    ```bash
    source venv/bin/activate
    ```

To deactivate the virtual environment, simply run:
```bash
deactivate
```

### Step 3: Install Django and Check Installed Packages

With the virtual environment activated, install Django using pip:
```bash
pip install django
```

To check the installed packages, use:
```bash
pip list
```

To freeze the installed packages into a `requirements.txt` file, use:
```bash
pip freeze > requirements.txt
```

### Step 4: What is `django-admin`?

`django-admin` is a command-line utility that comes with Django. It helps you perform various tasks such as creating new projects, running the development server, and managing applications.

### Step 5: Create a Django Project

Create a new Django project using the `django-admin` command:
```bash
django-admin startproject mysite .
```

This will create a directory structure as follows:
```
.mysite/
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py
manage.py
```

- **`__init__.py`**: An empty file that tells Python that this directory should be considered a package.
- **`asgi.py`**: Entry-point for ASGI-compatible web servers to serve your project.
- **`settings.py`**: Configuration file for your Django project.
- **`urls.py`**: URL declarations for your Django project; a "table of contents" of your Django-powered site.
- **`wsgi.py`**: Entry-point for WSGI-compatible web servers to serve your project.
- **`manage.py`**: A command-line utility that lets you interact with this Django project in various ways.

Now you have successfully created your first Django project!

## Fundamentals of Django

Django is built on the principle of "Don't Repeat Yourself" (DRY), which means it encourages the reuse of code and focuses on automating as much as possible. Here are some fundamental concepts:

- **Models**: Define the structure of your database.
- **Views**: Handle the logic of your application.
- **Templates**: Render the HTML pages.
- **URLs**: Route the requests to the appropriate view.

## Django Settings Explained

The `settings.py` file contains all the configuration for your Django project. Some important settings include:

- **DEBUG**: A boolean that turns on/off debug mode.
- **INSTALLED_APPS**: A list of all Django applications that are activated in this project.
- **MIDDLEWARE**: A list of middleware to use.
- **DATABASES**: Configuration for your database.
- **TEMPLATES**: Configuration for your templates.

## How Django Works

Django follows the Model-View-Template (MVT) architecture:

1. **Request**: The user makes a request to the server.
2. **URL Routing**: Django uses the URLconf to route the request to the appropriate view.
3. **View**: The view processes the request, interacts with the model, and renders a template.
4. **Response**: The rendered template is sent back to the user as an HTTP response.

## URLs and HttpResponse

In Django, you define URL patterns in the `urls.py` file. Each pattern is associated with a view function. For example:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

The view function might look like this:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world!")
```

## Implement Django Template

Django templates allow you to create dynamic HTML pages. Here's a simple example:

1. **Create a Template**: Create an HTML file in a `templates` directory.
    ```html
    <!-- templates/home.html -->
    <h1>Welcome to My Site</h1>
    ```

2. **Render the Template**: Modify the view to render the template.
    ```python
    from django.shortcuts import render

    def home(request):
        return render(request, 'home.html')
    ```

## Implement Bootstrap and Tailwind

To use Bootstrap or Tailwind CSS in your Django project, you need to include their CSS files in your templates.

### Bootstrap

1. **Include Bootstrap CSS**:
    ```html
    <!-- templates/base.html -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    ```

2. **Use Bootstrap Classes**:
    ```html
    <!-- templates/home.html -->
    {% extends 'base.html' %}
    {% block content %}
    <div class="container">
        <h1 class="text-center">Welcome to My Site</h1>
    </div>
    {% endblock %}
    ```

### Tailwind

1. **Include Tailwind CSS**:
    ```html
    <!-- templates/base.html -->
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.0.2/dist/tailwind.min.css" rel="stylesheet">
    ```

2. **Use Tailwind Classes**:
    ```html
    <!-- templates/home.html -->
    {% extends 'base.html' %}
    {% block content %}
    <div class="container mx-auto">
        <h1 class="text-center text-4xl">Welcome to My Site</h1>
    </div>
    {% endblock %}
    ```

## Django Static Files

Django handles static files (CSS, JavaScript, images) using the `STATICFILES_DIRS` and `STATIC_URL` settings in `settings.py`.

1. **Configure Static Files**:
    ```python
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [BASE_DIR / "static"]
    ```

2. **Create a Static Directory**: Create a `static` directory in your project root and add your static files there.

3. **Include Static Files in Templates**:
    ```html
    <!-- templates/base.html -->
    {% load static %}
    <link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
    ```

## Additional Resources

For more in-depth learning, consider the following resources:

- [Official Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/en/)
- [Mozilla Developer Network Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
- [Real Python Django Tutorials](https://realpython.com/tutorials/django/)
- [Django for Beginners Book](https://djangoforbeginners.com/)

By following these steps and utilizing these resources, you can effectively learn and master Django.

## Creating a Simple Django To-Do App

### Stage 1: Installation and Setup

In this stage, we will create a folder for our project, set up a virtual environment, install Django, and run the app.

#### Step 1: Create a Project Folder

First, create a folder for your project. Open your terminal and run:
```bash
mkdir django_todo
cd django_todo
```

#### Step 2: Set Up a Virtual Environment

Create and activate a virtual environment:
```bash
python -m venv .venv
```

- On Windows:
    ```bash
    venv\Scripts\activate
    ```
- On macOS and Linux:
    ```bash
    source venv/bin/activate
    ```

#### Step 3: Install Django

With the virtual environment activated, install Django:
```bash
pip install django
```

#### Step 4: Create a Django Project

Create a new Django project named `todo`:
```bash
django-admin startproject todo .
```

#### Step 5: Run the Development Server

Navigate to the project directory and run the development server:
```bash
python manage.py runserver
```

Open your web browser and go to `http://127.0.0.1:8000/` to see the default Django welcome page.

You have successfully set up your Django project and run the development server. In the next stages, we will create the To-Do app and add functionalities.