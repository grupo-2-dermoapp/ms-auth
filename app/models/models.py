from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy import Date, Enum
from datetime import datetime
from app.utils.utils import uuid4Str
from .emums import *
from app import db



class Doctor(db.Model):
    uuid = Column(String(40), primary_key=True, default=uuid4Str)
    email = Column(String(40), unique=True)
    names = Column(String(50))
    surnames = Column(String(40))
    password = Column(String(200))
    medical_license = Column(String(200))
    is_active = Column(Boolean(), default=False)
    created_at = Column(DateTime, default=datetime.now())

class DoctorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Doctor
        exclude = ('password', 'created_at', 'is_active')
        load_instance = True
        include_relationships = True

class Patient(db.Model):
    uuid = Column(String(40), primary_key=True, default=uuid4Str)
    email = Column(String(40), unique=True)
    names = Column(String(50))
    location = Column(String(50))
    password = Column(String(200))
    dermatological_profile_uuid = Column(String(40), ForeignKey('dermatological_profile.uuid'))
    is_active = Column(Boolean(), default=True)
    created_at = Column(DateTime, default=datetime.now())

class PatientSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Patient
        exclude = ('password', 'created_at', 'is_active')
        load_instance = True
        include_relationships = True


class DermatologicalProfile(db.Model):
    uuid = Column(String(40), primary_key=True, default=uuid4Str)
    eyes_color = Column(Enum(EyesColor))
    hair_color = Column(Enum(HairColor))
    skin_color = Column(Enum(SkinColor))
    freckles = Column(Enum(Freckles))
    skin_stay_in_the_sun = Column(Enum(SkinStayInTheSun))
    turn_brown = Column(Enum(TurnBrown))
    how_brown = Column(Enum(HowBrown))
    face_sensitive = Column(Enum(FaceSensitive))
    how_often_tan = Column(Enum(HowOftenTan))
    artificial_time_expose = Column(Enum(ArtificialTimeExpose))
    patient = db.relationship('Patient', backref='dermatological_profile')

class DermatologicalProfileSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = DermatologicalProfile
        load_instance = True
        include_relationships = True