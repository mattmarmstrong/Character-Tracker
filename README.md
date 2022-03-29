# 370 Project Group 43 #

Character Tracker

A website designed with the purpose of letting players of a
roleplaying game keep track of their character and keep notes.

## Required Libraries and Programs ##

- python version 3.10

- django version 4.0.3

- django-multiselectfield version 0.1.12

## Installation And Running Instruction ##

1. Download the source code files

2. Put the downloaded files into the desired location

3. Enter your command line, command prompt, or shell of choice

4. Change the current directory to the location of the main folder

5. Type into the command line the prompt "python manage.py runserver"


## Important Files and Folders ##

Folders
---------------------------------------------------

proto: 	location of the main .py files used by the website

static:	location of all the .css files and images the website uses

templates:	location of the 'main.html' and 'navbar.html' templates

base:	location of the templates and forms that make the website
		run and function properly

base\templatetags:	Folder for dev defined tags and filters
------------------------------------------------------

Files
------------------------------------------------------

manage.py: 			used for admin tasks for django after calling
					python


db.sqlite3:			The database where all the website's data is
					stored


proto\settings.py: 	file detailing the settings of the project
					including apps it can use and root file locations


[folder]\urls.py:	files listing out the urls and their names


base\models.py:		the file where develper defined models are writen
					and stored


base\views.py:		the file where webpage logic and data are
					declared and used by django

base\forms.py		the page where forms are set for use by django


base\apps.py		the file where the apps the webpages will use
					are declared and or implimented


## How to setup and login to an Admin Account ##

1. Have the main project setup and functioning

2. In the command ling/prompt/sheel of your choice, type in the
command 'python manage.py createsuperuser'

3. Enter in the desired username, email address, and password as
prompted

4. Open your web browser of choice and open the url of the website
with a "/admin" after it like "[url of site]/admin"

5. Login to the new admin account and moderate the website as you
see fit