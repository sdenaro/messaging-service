"""
App
"""

from flask import Flask
from config import Config
from .models.db import db
from .routes.messages import app as messages_bp

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        #db.commit()
        print("Database created!")

    app.register_blueprint(messages_bp)

    return app
