from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

path = os.path.dirname( os.path.realpath(__file__) )
database_path = os.path.join(path, 'mydb.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))

    def __init__(self, username, password):
        self.username = username
        self.password = password

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
	print users
	usernames = [ user.username for user in users ]
	return render_template('index.html', usernames=usernames)