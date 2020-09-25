import uuid
import datetime

from app.main import db
from app.main.model.level import Level


def save_new_level(data):
    level = Level.query.filter_by(name = data['name']).first()
    if not level:
        new_level = Level(        			
			name = data['name'],
			description = data['description']
        )
        save_changes(new_level)
        return generate_token(new_level)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Level already exists. Please insert another.',
        }
        return response_object, 409


def get_all_levels():
    return Level.query.all()


def get_a_level(name):
    return Level.query.filter_by(name = nameº).first()

def delete_a_level(name):
    return Level.query.filter_by(name = name).delete()    


def update_a_level(data):
    level = Level.query.filter_by(name = data['name']).first()
    level.description = data['description']
    db.session.commit()
    return 201    

def generate_token(level):
    try:
        # generate the auth token
        auth_token = Level.encode_auth_token(level.id)
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

