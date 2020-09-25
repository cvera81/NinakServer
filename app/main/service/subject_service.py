import uuid
import datetime

from app.main import db
from app.main.model.subject import Subject


def save_new_subject(data):
    subject = Subject.query.filter_by(short_name=data['short_name']).first()
    if not subject:
        new_subject = Subject(        
			id_area = data['id_area'],
            short_name = data['short_name'],
			name = data['name']			
        )
        save_changes(new_subject)
        return generate_token(new_subject)
    else:
        response_object = {
            'status': 'fail',
            'message': 'new_achievement already exists. Please insert another.',
        }
        return response_object, 409


def get_all_subjects():
    return Subject.query.all()


def get_a_subject(short_name):
    return Subject.query.filter_by(short_name = short_name).first()

def delete_a_subject(short_name):
    return Subject.query.filter_by(short_name = short_name).delete()    


def update_a_subject(data):
    subject = Subject.query.filter_by(short_name = data['short_name']).first()
    subject.name=data['name']
    db.session.commit()
    return 201    

def generate_token(subject):
    try:
        # generate the auth token
        auth_token = Subject.encode_auth_token(subject.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()

