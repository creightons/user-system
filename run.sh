#!/bin/sh
export FLASKR_SETTINGS=./settings.cfg
FLASK_APP=server.py flask run
