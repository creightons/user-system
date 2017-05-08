# user-system

## Synopsis

A simple web-app implementing a permissions-based access control system. Every user created in the app has access to a private area. However, to access certain pages the user must have the appropriate permission. Built using Flask and Python 2.7.

## Instructions

- Clone the project from github

- Open a terminal and change directory to the project's root 

- User virtualenv to create an isolated environment `virtualenv venv`

- Activate the virtual env `venv/Scripts/activate` (on Windows)

- Install all dependencies with pip `pip install -r requirements.txt`

- Create the SQLITE database `./make-db.sh` (Needs to be run from a Bash shell)

- Run the application `./run.sh` (Needs to be run from a Bash shell)

- Open a browser and go to localhost:5000 to open the app
