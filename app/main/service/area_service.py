import uuid
import datetime

from app.main import db
from app.main.model.area import Area


def save_new_area(data):
    area = Area.query.filter_by(short_name=data['short_name']).first()
    if not area:
        new_area = Area(        
			short_name = data['short_name'],
			name = data['name'],
			description = data['description']
        )
        save_changes(new_area)
        return generate_token(new_area)
    else:
        response_object = {
            'status': 'fail',
            'message': 'new_achievement already exists. Please insert another.',
        }
        return response_object, 409


def get_all_areas():
    return Area.query.all()


def get_an_area(short_name):
    return Area.query.filter_by(short_name = short_name).first()

def delete_an_area(short_name):
    return Area.query.filter_by(short_name = short_name).delete()    


def update_an_area(data):
    area = Area.query.filter_by(short_name = data['short_name']).first()
    area.name=data['name']
    db.session.commit()
    return 201    

def generate_token(area):
    try:
        # generate the auth token
        auth_token = Area.encode_auth_token(area.id)
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

