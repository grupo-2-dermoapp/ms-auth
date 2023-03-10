from app.views.views import DoctorRegister, PatientRegister
from app.views.views import DermatologicalProfileRegister, Health
from app.views.views import PatientLogin
from app.views.views import DoctorLogin


from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_cors import CORS
from app import create_app
from flask import jsonify
from flask_migrate import Migrate
from flask_migrate import upgrade
from app import db
import os

import pytest

@pytest.fixture()
def app():

    # settings_module = os.getenv('APP_SETTINGS_MODULE')
    settings_module = 'config.develop.Test'
    app = create_app(settings_module)
    db.init_app(app)

    api = Api(app)
    CORS(app)

    api.add_resource(Health, "/dermoapp/auth/v1/health")
    api.add_resource(DoctorRegister, "/dermoapp/auth/v1/doctor-register")
    api.add_resource(PatientRegister, "/dermoapp/auth/v1/patient-register")
    api.add_resource(PatientLogin, "/dermoapp/auth/v1/patient-login")
    api.add_resource(DoctorLogin, "/dermoapp/auth/v1/doctor-login")

    api.add_resource(DermatologicalProfileRegister, "/dermoapp/auth/v1/dermo-profile-register")
    with app.app_context():
            upgrade()

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()