from flask import Flask
import os
app = Flask(__name__)

path = os.path.dirname( os.path.realpath(__file__) )
database_path = os.path.join(path, '../mydb.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path

from database import db

# Initialize Database
db.init_app(app)

from routes import apply_routes
apply_routes(app)