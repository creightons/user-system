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
		usernames = [ user.username for user in users ]

		return render_template('index.html', usernames=usernames)