from flask import Flask, render_template, request
import os

app = Flask(__name__)

path = os.path.dirname( os.path.realpath(__file__) )
database_path = os.path.join(path, '../mydb.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path

from database import db

# Initialize Database
db.init_app(app)

# Import models after database is initialized
from models.user import User

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