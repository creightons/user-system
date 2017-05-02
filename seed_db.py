from application.database import db
from application.server import app

def add_users(db, users):
	for row in user_data:
		user = models.User(row['username'], row['password'])
		db.session.add(user)

def add_permissions(db, permissions):
	for row in permissions:
		permission = models.Permission(row['id'], row['description'])
		db.session.add(permission)

user_data = [
	{ 'username': 'user1', 'password': 'pass1' },
	{ 'username': 'user2', 'password': 'pass2' },
	{ 'username': 'user3', 'password': 'pass3' },
	{ 'username': 'user4', 'password': 'pass4' },
	{ 'username': 'user5', 'password': 'pass5' },
	{ 'username': 'user6', 'password': 'pass6' },
	{ 'username': 'user7', 'password': 'pass7' },
]

permission_data = [
	{ 'id': 1, 'description': 'Permission 1', },
	{ 'id': 2, 'description': 'Permission 2', },
	{ 'id': 3, 'description': 'Permission 3', },
	{ 'id': 4, 'description': 'Permission 4', },
	{ 'id': 5, 'description': 'Permission 5', },
]



with app.test_request_context():
	from application import models
	add_users(db, user_data)
	add_permissions(db, permission_data)
	db.session.commit()