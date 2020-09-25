import uuid
import datetime

from app.main import db
from app.main.model.achievement import Achievement


def save_new_achievement(data):
    achievement = Achievement.query.filter_by(short_name=data['short_name']).first()
    if not achievement:
        new_achievement = Achievement(        
			short_name = data['short_name'],
			name = data['name'],
			description = data['description']
        )
        save_changes(new_achievement)
        return generate_token(new_achievement)
    else:
        response_object = {
            'status': 'fail',
            'message': 'new_achievement already exists. Please insert another.',
        }
        return response_object, 409


def get_all_achievements():
    return Achievement.query.all()


def get_an_achievement(short_name):
    return Achievement.query.filter_by(short_name = short_name).first()

def delete_an_achievement(short_name):
    return Achievement.query.filter_by(short_name = short_name).delete()    


def update_an_achievement(data):
    achievement = Achievement.query.filter_by(short_name = data['short_name']).first()
    achievement.name=data['name']
    db.session.commit()
    return 201    

def generate_token(achievement):
    try:
        # generate the auth token
        auth_token = Achievement.encode_auth_token(achievement.id)
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

