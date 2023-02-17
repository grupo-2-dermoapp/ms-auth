from app.models.models import Patient, Doctor, DermatologicalProfile
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

def test_doctor_login_without_params(client):
    response = client.post("/dermoapp/auth/v1/doctor-login")
    data = response.json
    status = response.status
    print(data)
    print(status)
    assert data['message'] == 'The browser (or proxy) sent a request that this server could not understand.'
    assert status == '400 BAD REQUEST'

def test_doctor_login_with_good_credentials(client, app):
    clear_doctor_table(app)
    doctor = create_doctor(app)

    response = client.post("/dermoapp/auth/v1/doctor-login", json={
        "email": 'test@test.com',
        "password": 'test'
    })
    
    data = response.json
    status = response.status
    print(data)
    print(status)

    assert data['message'] == 'Login correcto'
    assert status == '200 OK'
    

def clear_doctor_table(app):
    with app.app_context():
        doctors = Doctor.query.all()
        for doctor in doctors:
            db.session.delete(doctor)
            db.session.commit()
            db.session.close()

def create_doctor(app):
    password_hash = generate_password_hash('test')
    doctor = Doctor(
        email = 'test@test.com',
        password = password_hash,
    
    )

    with app.app_context():
        db.session.add(doctor)
        db.session.commit()
        db.session.close()

    return doctor

