from application.database import db
from application.server import app

user_data = [
	{ 'username': 'user1', 'password': 'pass1' },
	{ 'username': 'user2', 'password': 'pass2' },
	{ 'username': 'user3', 'password': 'pass3' },
	{ 'username': 'user4', 'password': 'pass4' },
	{ 'username': 'user5', 'password': 'pass5' },
	{ 'username': 'user6', 'password': 'pass6' },
]

with app.test_request_context():
	from application import models

	for row in user_data:
		user = models.User(row['username'], row['password'])
		db.session.add(user)

	db.session.commit()