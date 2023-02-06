from app.models.models import Patient, Doctor, DermatologicalProfile
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

def test_login_without_params(client):
    response = client.post("/dermoapp/auth/v1/patient-login")
    data = response.json
    code = response.status
    assert data['message'] == 'The browser (or proxy) sent a request that this server could not understand.'
    assert code == '400 BAD REQUEST'

def test_login_with_good_credentials(client, app):
    clear_patients_table(app)
    password_hash = generate_password_hash('test')
    
    patient = Patient(
        email = 'test@test.com',
        names = 'names test',
        age = 18,
        location = 'New York',
        password = password_hash)
    
    with app.app_context():
        db.session.add(patient)
        db.session.commit()
        db.session.close()

    response = client.post("/dermoapp/auth/v1/patient-login", json={
        "email": 'test@test.com',
        "password": 'test'
    })
    
    data = response.json
    status = response.status
    assert data['message'] == 'Login correcto'
    assert status == '200 OK'
    

def clear_patients_table(app):
    with app.app_context():
        patients = Patient.query.all()
        for patient in patients:
            db.session.delete(patient)
            db.session.commit()
            db.session.close()


