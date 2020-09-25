import uuid
import datetime

from app.main import db
from app.main.model.achievement_trans import Achievement_trans


def save_new_achievement_trans(data):
    achievement_trans = Achievement_trans.query.filter_by(id_achievement = data['id_achievement']).first()
    if not achievement_trans:
        new_achievement_trans = Achievement_trans(        
			id_achievement = data['id_achievement'],
			id_account = data['id_account'],
			registered_on = datetime.datetime.utcnow()
        )
        save_changes(new_achievement_trans)
        return generate_token(new_achievement_trans)
    else:
        response_object = {
            'status': 'fail',
            'message': 'new_achievement_trans already exists. Please insert another.',
        }
        return response_object, 409


def get_all_achievements_trans():
    return Achievement_trans.query.all()


def get_an_achievement_trans(id_achievement):
    return Achievement_trans.query.filter_by(id_achievement = id_achievement).first()

def delete_an_achievement_trans(id_achievement):
    return Achievement_trans.query.filter_by(id_achievement = id_achievement).delete()    


def update_an_achievement_trans(data):
    achievement_trans = Achievement_trans.query.filter_by(id_achievement = data['id_achievement']).first()
    Achievement_trans.registered_on = datetime.datetime.utcnow()
    db.session.commit()
    return 201    

def generate_token(achievement_trans):
    try:
        # generate the auth token
        auth_token = Achievement_trans.encode_auth_token(achievement_trans.id)
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

