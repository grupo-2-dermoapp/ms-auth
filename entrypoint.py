from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_cors import CORS
from app import create_app
from flask import jsonify
from flask_migrate import Migrate

from app.views.views import DoctorRegister, PatientRegister
from app.views.views import DermatologicalProfileRegister, Health
from app.views.views import PatientLogin
import os

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)

api = Api(app)
CORS(app)

api.add_resource(Health, "/dermoapp/auth/v1/health")
api.add_resource(DoctorRegister, "/dermoapp/auth/v1/doctor-register")
api.add_resource(PatientRegister, "/dermoapp/auth/v1/patient-register")
api.add_resource(PatientLogin, "/dermoapp/auth/v1/patient-login")
api.add_resource(DermatologicalProfileRegister, "/dermoapp/auth/v1/dermo-profile-register")



if __name__ == '__main__':
    app.run()