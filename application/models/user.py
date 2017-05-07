from application.database import db
from user_permissions import user_permissions

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))
    permissions = db.relationship(
    	'Permission',
    	secondary=user_permissions,
    	backref=db.backref('users', lazy='dynamic')
	)

    def __init__(self, username, password):
        self.username = username
        self.password = password