from database import db
from server import app

db.init_app(app)

from routes import apply_routes

apply_routes(app)