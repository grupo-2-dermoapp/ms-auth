# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request, current_app
import validators
import requests
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from app.models.models import Patient, Doctor, DermatologicalProfile, db
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import os
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, create_refresh_token
import datetime
from flask_jwt_extended.view_decorators import jwt_required
from flask_jwt_extended import get_jwt_identity, get_jwt
import json
from app.utils.utils import allowed_file
import app


class Health(Resource):
    def get(self):
        data = {
            "message" : "OK"
        }
        return data, 200

class DoctorRegister(Resource):
    def post(self):
        request_data = request.form
        request_image = request.files['medical_license']
        email = request_data['email'].replace(" ", "").lower()
        try:
            if not validators.email(email):
                data = {
                    "code" : "1003",
                    "message" : "Correo electrónico no válido"       
                }
                return  data, 400

            if not allowed_file(request_image.filename):
                data = {
                    "code" : "1004",
                    "message" : "Archivo no válido"       
                }
                return  data, 400

            password_hash = generate_password_hash(request_data['password'])
            filename = secure_filename(request_image.filename)
            file_path = os.path.join(os.getenv('UPLOAD_FOLDER'), filename)
            request_image.save(file_path)
            doctor = Doctor(
                email = email,
                names = request_data['names'],
                surnames = request_data['surnames'],
                nationality = request_data['nationality'],
                speciality = request_data['speciality'],
                password = password_hash,
                medical_license = file_path)

            db.session.add(doctor)
            db.session.commit()
    
            data = {
                "code": "1000",
                "message" : "Usuario creado correctamente",
                "user" : {
                    "uuid" : str(doctor.uuid),
                    "email" : doctor.email,
                }
            }  
            return data, 201
        except KeyError:
            db.session.rollback()
            data = {
                "code" : "1001",
                "message" : "Falla en el registro"
                }
            return data, 400
        
        except IntegrityError as e:
            db.session.rollback()
            data = {
                "code" : "1002",
                "message" : "El correo electrónico ya se encuentra registrado en la plataforma"
                }
            return data, 400
        finally:
            db.session.close()

class PatientRegister(Resource):
    def post(self):
        request_data = request.json
        email = request_data['email'].replace(" ", "").lower()
        try:
            if not validators.email(email):
                data = {
                    "code" : "1013",
                    "message" : "Correo electrónico no válido"       
                }
                return  data, 400

            password_hash = generate_password_hash(request_data['password'])
            patient = Patient(
                email = email,
                names = request_data['names'],
                age = request_data['age'],
                location = request_data['age'],
                password = password_hash)

            if request_data['dermatological_profile_uuid']:
                patient.dermatological_profile_uuid = request_data['dermatological_profile_uuid']
            
            db.session.add(patient)
            db.session.commit()
    
            data = {
                "code": "1010",
                "message" : "Usuario creado correctamente",
                "user" : {
                    "uuid" : str(patient.uuid),
                    "email" : patient.email,
                }
            }  
            return data, 201
        except KeyError:
            db.session.rollback()
            data = {
                "code" : "1011",
                "message" : "Falla en el registro"
                }
            return data, 400
        
        except IntegrityError as e:
            db.session.rollback()
            data = {
                "code" : "1012",
                "message" : "El correo electrónico ya se encuentra registrado en la plataforma"
                }
            return data, 400
        finally:
            db.session.close()


class DermatologicalProfileRegister(Resource):
    def post(self):
        request_data = request.json
        try:
            dermatological_profile = DermatologicalProfile(
                eyes_color = request_data['eyes_color'],
                hair_color = request_data['hair_color'],
                skin_color = request_data['skin_color'],
                freckles = request_data['freckles'],
                skin_stay_in_the_sun = request_data['skin_stay_in_the_sun'],
                turn_brown = request_data['turn_brown'],
                how_brown = request_data['how_brown'],
                face_sensitive = request_data['face_sensitive'],
                how_often_tan = request_data['how_often_tan'],
                artificial_time_expose = request_data['artificial_time_expose'])

            db.session.add(dermatological_profile)
            db.session.commit()
    
            data = {
                "code": "1020",
                "message" : "Perfil dermatologico creado correctamente",
                "dermatological_data" : {
                    "uuid" : dermatological_profile.uuid
                }
            }  

            return data, 201


        except KeyError:
            db.session.rollback()
            data = {
                "code" : "1021",
                "message" : "Falla en el registro"
                }
            return data, 400

        finally:
            db.session.close()

class PatientLogin(Resource):
    def post(self):
        email = request.json['email']
        password = request.json['password']
        user = Patient.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):

                data = {
                    'code': '1100',
                    'message' : 'Login correcto',
                    'user' : {
                        'email' : user.email,
                        'names' : user.names,
                        'surnames' : user.surnames,
                    }
                }
                return data, 200
            else:
                data = {
                    'code' : '1101',    
                    'title' : 'Datos errados',
                    'message' : 'Verifica que las credenciales ingresadas sean correctas e inténtalo de nuevo.'
                    }
                return data, 401
                
        else:
            data = {
                'code' : '1102',
                'title' : 'Datos errados',
                'message' : 'Verifica que las credenciales ingresadas sean correctas e inténtalo de nuevo.'
                }
            return data, 401

