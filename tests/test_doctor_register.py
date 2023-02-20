from app.models.models import Patient, Doctor, DermatologicalProfile
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from pathlib import Path
from io import BytesIO, open

resources = Path(__file__).parent / "resources"

def test_doctor_register_without_params(client):
    response = client.post("/dermoapp/auth/v1/doctor-register")
    data = response.json
    code = response.status
    assert data['message'] == 'The browser (or proxy) sent a request that this server could not understand.'
    assert code == '400 BAD REQUEST'


def test_doctor_register_ok(client, app):
    clear_doctor_table(app)
    doctor = {}
    doctor['email'] = 'test@test.com'
    doctor['names'] = 'Usuario Test'
    doctor['nationality'] = 'American'
    doctor['speciality'] = 'faces'
    doctor['password'] = 'test'
    doctor['medical_license'] = (BytesIO(b"abcdef"), 'test.pdf')

    response = client.post("/dermoapp/auth/v1/doctor-register", content_type='multipart/form-data', data=doctor)
    
    data = response.json
    status = response.status
    assert data['code'] == '1000'
    assert status == '201 CREATED'

def test_doctor_register_invalid_email(client, app):
    clear_doctor_table(app)
    doctor = {}
    doctor['email'] = 'test'
    doctor['names'] = 'Usuario Test'
    doctor['nationality'] = 'American'
    doctor['speciality'] = 'faces'
    doctor['password'] = 'test'
    doctor['medical_license'] = (BytesIO(b"abcdef"), 'test.pdf')

    response = client.post("/dermoapp/auth/v1/doctor-register", content_type='multipart/form-data', data=doctor)
    
    data = response.json
    status = response.status
    assert data['code'] == '1003'
    assert status == '400 BAD REQUEST'
    

def clear_doctor_table(app):
    with app.app_context():
        doctors = Doctor.query.all()
        for doctor in doctors:
            db.session.delete(doctor)
            db.session.commit()
            db.session.close()


