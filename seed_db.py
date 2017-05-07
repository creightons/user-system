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

def add_user_permissions(db, user_permissions_data):
	for row in user_permissions_data:
		db.session.connection().execute(
			models.user_permissions.insert().values(
				userid=row['userid'],
				permissionid=row['permissionid']
			)
		)


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

user_permissions_data = [
	{ 'userid': 1, 'permissionid': 1 },
	{ 'userid': 1, 'permissionid': 2 },
	{ 'userid': 1, 'permissionid': 3 },
	{ 'userid': 1, 'permissionid': 4 },
]


with app.test_request_context():
	from application import models
	add_users(db, user_data)
	add_permissions(db, permission_data)
	add_user_permissions(db, user_permissions_data)
	db.session.commit()