# Nba Matchups Dashboard 
![Twitter Follow](https://img.shields.io/twitter/follow/checkballnba?style=social)

A Python driven web app and TwitterBot for comparing team data. 
Choose an NBA team, view their stats, and see how they matchup
against each other.
 
* * Python version:  python-3.8.10

### Table of Contents
* [Demo](#demo)
* [Docker setup](#docker-support)  
* [Quickstart](#quick-start)  
* [Documentation](#documentation)
* [File Structure](#file-structure)
* [Report an Issue](#reporting-issues)
* [Credits](#credits)

### Demo
 A live demo of this page is [coming soon]()

## Docker Support

> Get the code

```bash
$ git clone https://github.com/tmeralus/nba-matchups.git
$ cd nba-matchups
```

> Start the app in Docker

```bash
$ docker-compose pull   # download dependencies 
$ docker-compose build  # local set up
$ docker-compose up -d  # start the app 
```

Visit `http://localhost:85` in your browser. The app should be up & running.

## Quick Start

> UNZIP the sources or clone the private repository. After getting the code, open a terminal and navigate to the working directory, with product source code.

```bash
$ # Get the code
$ git clone https://github.com/tmeralus/nba-matchups.git
$ cd argon-dashboard-flask
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Database
$ # pip3 install -r requirements.txt
$
$ # OR with PostgreSQL connector
$ pip3 install -r requirements-pgsql.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ # (Windows) set FLASK_APP=run.py
$ # (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Start the application (development mode)
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the dashboard in browser: http://127.0.0.1:5000/
```

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.


## File Structure
Within the download you'll find the following directories and files:

```bash
< PROJECT ROOT >
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- routes.py                 # Define app routes
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- routes.py                 # Define authentication routes  
   |    |    |-- models.py                 # Defines models  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |    |    |-- includes/                 # HTML chunks and components
   |    |    |    |-- navigation.html      # Top menu component
   |    |    |    |-- sidebar.html         # Sidebar component
   |    |    |    |-- footer.html          # App Footer
   |    |    |    |-- scripts.html         # Scripts common to all pages
   |    |    |
   |    |    |-- layouts/                   # Master pages
   |    |    |    |-- base-fullscreen.html  # Used by Authentication pages
   |    |    |    |-- base.html             # Used by common pages
   |    |    |
   |    |    |-- accounts/                  # Authentication pages
   |    |    |    |-- login.html            # Login page
   |    |    |    |-- register.html         # Register page
   |    |    |
   |    |    |-- home/                      # UI Kit Pages
   |    |         |-- index.html            # Index page
   |    |         |-- 404-page.html         # 404 page
   |    |         |-- *.html                # All other pages
   |    |    
   |  config.py                             # Set up the app
   |    __init__.py                         # Initialize the app
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |-- requirements-mysql.txt               # Production modules  - Mysql DMBS
   |-- requirements-pqsql.txt               # Production modules  - PostgreSql DMBS
   |
   |-- Dockerfile                           # Deployment
   |-- docker-compose.yml                   # Deployment
   |-- gunicorn-cfg.py                      # Deployment   
   |-- nginx                                # Deployment
   |    |-- Tedley-app.conf                # Deployment 
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- run.py                               # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```
 ---

##### Reporting Issues

I use GitHub Issues as the official bug tracker for the **NBA Matchups Dashboard**. Here are some advice for users that want to report an issue:

1. Make sure that you are using the latest version of the **NBA Matchups Dashboard**. Check the Version number from your dashboard in the footer.
2. Please provide reproducible steps for the issue to help shorten the time it takes for it to be fixed.
3. Some issues may be browser-specific, so specifying in what browser you encountered the issue might help.
4. Sumbit through github Issues
 
- Issues: [Github Issues Page](https://github.com/tmeralus/nba-matchups/issues)

---
 
#### Browser Support

At present, we officially aim to support the last two versions of the following browsers:

<img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/chrome.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/firefox.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/edge.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/safari.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/opera.png" width="64" height="64">

#### Credits 
Theme originally developed by [Creative Tim](https://www.creative-tim.com/product/argon-dashboard-flask) 

You can click here to find the [Free Argon Dashboard Flask](https://github.com/creativetimofficial/argon-dashboard-flask)

