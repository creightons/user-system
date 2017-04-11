from flask import Flask, session, request, escape, redirect, url_for
app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def index():
	if 'username' in session:
		return 'Logged in as %s' % escape(session['username'])
	return '''
		<div>Greetings</div>
		<a href='/login'>Go to Login</a>
	'''



@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('index'))

	# GET
	return '''
		<form method='post'>
			<p><input type=text name=username>
			<p><input type=submit value=Login>
		</form>
	'''

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))