from app.models.models import Patient, Doctor, DermatologicalProfile
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

def test_dermatological_profile_without_params(client):
    response = client.post("/dermoapp/auth/v1/dermo-profile-register")
    data = response.json
    code = response.status
    assert data['message'] == 'The browser (or proxy) sent a request that this server could not understand.'
    assert code == '400 BAD REQUEST'


def test_dermatological_profile_ok(client, app):
    clear_dermatological_profile_table(app)
    profile = {}
    profile['eyes_color'] = 'LIGHT_BLUE_GREEN_GREY'
    profile['hair_color'] = 'RED'
    profile['skin_color'] = 'PINK'
    profile['freckles'] = 'MANY'
    profile['skin_stay_in_the_sun'] = 'SEVERE_BURNS'
    profile['turn_brown'] = 'NEVER'
    profile['how_brown'] = 'HARDLY'
    profile['face_sensitive'] = 'VERY_SENSITIVE'
    profile['how_often_tan'] = 'NEVER'
    profile['artificial_time_expose'] = 'MORE_THREE_MONTHS'

    response = client.post("/dermoapp/auth/v1/dermo-profile-register", json=profile)
    
    data = response.json
    status = response.status
    print(data)
    print(status)
    assert data['code'] == '1020'
    assert status == '201 CREATED'
    

def clear_dermatological_profile_table(app):
    with app.app_context():
        profiles = DermatologicalProfile.query.all()
        for profile in profiles:
            db.session.delete(profile)
            db.session.commit()
            db.session.close()


