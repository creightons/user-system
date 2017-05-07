from __future__ import print_function # Print goes to STDERR
import sys
from flask import request, render_template, redirect
from models import User, Permission, user_permissions
from database import db

# Print data to STDERR in Flask terminal
def pr(arg):
	print(arg, file=sys.stderr)

def apply_routes(app):
	@app.route('/', methods=['GET', 'POST'])
	def index():
	#	return "Welcome to the main page"
		if request.method == 'POST':
			username = request.form['username']
			password = request.form['password']
			new_user = User(username, password)

			db.session.add(new_user)
			db.session.commit()

		users = User.query.all()
		user_data = [ { 'name': user.username, 'url': '/user_profile/' + str(user.id) } for user in users ]

		return render_template('index.html', user_data=user_data)


	@app.route('/user_profile/<user_id>')
	def user_route(user_id):
		user = User.query.filter(User.id == user_id).first()

		permissions = Permission.query.all()

		user_permission_map = { permission.id : True for permission in user.permissions }
		pr(user.permissions)

		permission_context = []

		for permission in permissions:
			permission_context.append({
				'id': permission.id,
				'description': permission.description,
				'user_has_permission': permission.id in user_permission_map,
			})

		context = {
			'username': user.username,
			'user_id': user.id,
			'permissions': permission_context,
		}

		return render_template('user_profile.html', context=context)

	@app.route('/permissions', methods=['POST'])
	def add_permissions():
		data = request.form
		user_id = data['user_id']
		# Convert new permission ids from string to int for comparison with existing permissions
		new_permission_id_list = [ int(new_id) for new_id in data.getlist('user_permission') ]
		user = User.query.get(user_id)

		# New Permission Ids are returned as Strings
		new_permission_id_hash = { permission_id : True for permission_id in new_permission_id_list }

		existing_permission_id_hash = { permission.id : True for permission in user.permissions }

		permissions_to_delete = [ permission for permission in user.permissions
			if permission.id not in new_permission_id_hash ]

		permission_ids_to_add = [ permission_id for permission_id in new_permission_id_list
			if permission_id not in existing_permission_id_hash ]

		if len(permission_ids_to_add) > 0 :
			for permission_id in permission_ids_to_add:
				db.session.connection().execute(
					user_permissions.insert().values(userid=user_id, permissionid=permission_id)
				)
			db.session.commit()

		if len(permissions_to_delete) > 0 :
			for permission in permissions_to_delete:
				user.permissions.remove(permission)
			db.session.commit()

		redirect_url = '/user_profile/' + data['user_id']

		return redirect(redirect_url)