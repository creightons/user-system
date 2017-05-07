from flask import session, redirect, flash
from models import User
from functools import wraps
from itertools import ifilter

def is_authorized(func):
	@wraps(func)

	def decorated_function(*args, **kwargs):
		# Make sure someone needs to sign in to access the decorated route
		if 'username' not in session:
			flash('ERROR: You must login to access this page')
			return redirect('/')

		return func(*args, **kwargs)

	return decorated_function



def check_permission(PERMISSION_ID):
	def permission_decorator(func):
		@wraps(func)

		def decorated_function(*args, **kwargs):
			user = User.query.filter_by(username=session['username']).first()

			# If the user has the correct permission to visit a page, grant
			# access. Otherwise redirect the user to the main page.
			try:
				next(ifilter(
					lambda permission: permission.id == PERMISSION_ID,
					user.permissions
				))
				return func(*args, **kwargs)
			except StopIteration:
				flash('ERROR: You are not authorized to access this page')
				return redirect('/main')

		return decorated_function

	return permission_decorator