print 'hi'
from app.main import setup_app
import os

print "settings = ", os.environ['FLASKR_SETTINGS']
app = setup_app()