from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(settings_module):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(settings_module)
    if not app.config.get('TESTING', False):
        app.config.from_pyfile('production.py', silent=True)
    else:
        app.config.from_pyfile('stage.py', silent=True)

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    return app