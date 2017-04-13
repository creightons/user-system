from flask import Flask 
from views import setup_routes

def setup_app():
	app = Flask(__name__)
	app.config.from_envvar('FLASKR_SETTINGS', silent=False)
	setup_routes(app)

	return app