from application.database import db

class Permission(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(200))