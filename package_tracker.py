from flask import Flask

from flask_migrate import Migrate

from app.models import db

from config import Configuration
from routes import tracker

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(tracker.bp)
db.init_app(app)
migrate = Migrate(app, db)
