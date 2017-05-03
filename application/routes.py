from flask import request, render_template
from models import User
from database import db

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
		context = {
			'username': user.username,
			'id': user.id,
		}

		return render_template('user_profile.html', context=context)
