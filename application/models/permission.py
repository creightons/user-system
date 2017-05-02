from application.database import db

class Permission(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(200))

	def __init__(self, id, description):
		self.id = id
		self.description = description