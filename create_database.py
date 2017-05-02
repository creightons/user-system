from application.database import db
from application.server import app

with app.test_request_context():
	db.init_app(app)
	from application.models import *
	db.create_all()