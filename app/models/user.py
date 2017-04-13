from flask_sqlalchemy import flask_sqlalchemy

class User(db.model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String)
	password = db.Column(db.String)

	def __init__(self, username, password):
		self.username = username,
		self.password = password