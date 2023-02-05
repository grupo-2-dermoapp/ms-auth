#!/bin/bash
pip list
pwd
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
db
export APP_SETTINGS_MODULE=config.develop.Config
export FLASK_APP=entrypoint.py
flask run --host 0.0.0.0 --port 3010