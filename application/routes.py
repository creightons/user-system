from __future__ import print_function # Print goes to STDERR
import sys
from flask import request, render_template, redirect, session, flash
from models import User, Permission, user_permissions
from database import db
from route_middleware import is_authorized, check_permission
from constants import PERMISSION_ONE, PERMISSION_TWO, PERMISSION_THREE, \
	PERMISSION_FOUR, PERMISSION_FIVE

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

		logged_in = False
		current_user = None
		if session.get('username') != None:
			logged_in = True
			current_user = session['username']

		return render_template(
			'index.html',
			user_data=user_data,
			logged_in=logged_in,
			current_user=current_user
		)



	@app.route('/user_profile/<user_id>')
	def user_route(user_id):
		user = User.query.filter(User.id == user_id).first()

		permissions = Permission.query.all()

		user_permission_map = { permission.id : True for permission in user.permissions }

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



	@app.route('/login', methods=['POST'])
	def login():
		user = User.query.filter_by(
			username=request.form['username'],
			password=request.form['password']
		).first()

		if user == None:
			flash('ERROR: Invalid Credentials')
			return redirect('/')
		else:
			session['username'] = request.form['username']
			return redirect('/main')



	@app.route('/logout', methods=['POST'])
	def logout():
		session.pop('username', None)
		return redirect('/')



	@app.route('/main', methods=['GET'])
	@is_authorized
	def main():
		if 'username' not in session:
			return redirect('/')

		return render_template(
			'main.html',
			username=session['username']
		)



	@app.route('/permission-one', methods=['GET'])
	@is_authorized
	@check_permission(PERMISSION_ONE)
	def permission_one_page():
		return render_template('permission_page.html', permission_type='One')

	@app.route('/permission-two', methods=['GET'])
	@is_authorized
	@check_permission(PERMISSION_TWO)
	def permission_two_page():
		return render_template('permission_page.html', permission_type='Two')



	@app.route('/permission-three', methods=['GET'])
	@is_authorized
	@check_permission(PERMISSION_THREE)
	def permission_three_page():
		return render_template('permission_page.html', permission_type='Three')



	@app.route('/permission-four', methods=['GET'])
	@is_authorized
	@check_permission(PERMISSION_ONE)
	def permission_four_page():
		return render_template('permission_page.html', permission_type='Four')



	@app.route('/permission-five', methods=['GET'])
	@is_authorized
	@check_permission(PERMISSION_FIVE)
	def permission_five_page():
		return render_template('permission_page.html', permission_type='Five')