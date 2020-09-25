import uuid
import datetime

from app.main import db
from app.main.model.institute import Institute


def save_new_Institute(data):
    institute = Institute.query.filter_by(email = data['email']).first()
    if not institute:
        new_institute = Institute(        
			name = data['name'],
			email = data['email'],
			phone = data['phone'],			
			id_country = data['id_country'],
            id_city = data['id_city'],
			id_state = data['id_state'],			
            registered_on = datetime.datetime.utcnow()            
        )
        save_changes(new_institute)
        return generate_token(new_institute)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Institute already exists. Please try again with another institute.',
        }
        return response_object, 409


def get_all_institutes():
    return Institute.query.all()


def get_an_institute(email):
    return Institute.query.filter_by(email = email).first()

def delete_an_institute(email):
    return Institute.query.filter_by(email = email).delete()

def update_an_institute(data):
	institute = Institute.query.filter_by(email = data['email']).first()
	institute.name = data['name']

	db.session.commit()
	return 201    
    
def generate_token(institute):
    try:
        # generate the auth token
        auth_token = Institute.encode_auth_token(institute.id)
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

