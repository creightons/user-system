from flask import Flask, session, request, escape, redirect, url_for, \
	render_template
app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def index():
	if 'username' in session:
		#return 'Logged in as %s' % escape(session['username'])
		return render_template('main.html', logged_in=True, username=escape(session['username']))
	return render_template('main.html', loggin_in=False)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('index'))

	# GET
	return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))