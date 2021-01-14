from flask import Flask


from .config import Configuration
from .routes import tracker

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(tracker.bp)