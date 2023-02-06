from app.models.models import Patient, Doctor, DermatologicalProfile
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

def test_patient_register_without_params(client):
    response = client.post("/dermoapp/auth/v1/patient-register")
    data = response.json
    code = response.status
    assert data['message'] == 'The browser (or proxy) sent a request that this server could not understand.'
    assert code == '400 BAD REQUEST'


def test_patient_register_ok(client, app):
    clear_patients_table(app)
    patient = {}
    patient['email'] = 'test@test.com'
    patient['names'] = 'Usuario Test'
    patient['age'] = '18'
    patient['location'] = 'New York'
    patient['password'] = 'test'
    patient['dermatological_profile_uuid'] = ''

    response = client.post("/dermoapp/auth/v1/patient-register", json=patient)
    
    data = response.json
    status = response.status

    assert data['code'] == '1010'
    assert status == '201 CREATED'

def test_patient_register_duplicate(client, app):
    clear_patients_table(app)
    patient = {}
    patient['email'] = 'test@test.com'
    patient['names'] = 'Usuario Test'
    patient['age'] = '18'
    patient['location'] = 'New York'
    patient['password'] = 'test'
    patient['dermatological_profile_uuid'] = ''

    response1 = client.post("/dermoapp/auth/v1/patient-register", json=patient)
    response2 = client.post("/dermoapp/auth/v1/patient-register", json=patient)
    
    data1 = response1.json
    data2 = response2.json
    status1 = response1.status
    status2 = response2.status

    assert data1['code'] == '1010'
    assert status1 == '201 CREATED'
    assert data2['code'] == '1012'
    assert status2 == '400 BAD REQUEST'
    

def clear_patients_table(app):
    with app.app_context():
        patients = Patient.query.all()
        for patient in patients:
            db.session.delete(patient)
            db.session.commit()
            db.session.close()


