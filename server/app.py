from flask import Flask
from .config import db
from .models import Episode, Guest, Appearance

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        from .routes import bp
        app.register_blueprint(bp)
        db.create_all()

    return app