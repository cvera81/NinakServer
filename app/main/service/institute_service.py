import uuid
import datetime

from app.main import db
from app.main.model.institute import Institute


def save_new_institute(data):
    institute = Institute.query.filter_by(email=data['email']).first()
    if not institute:
        new_institute = Institute(        
			name=data['name'],
			email=data['email'],			
			id_country=data['id_country'],
			id_state=data['id_state'],
			id_city=data['id_city'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_institute)
        return generate_token(new_institute)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Institute already exists. Please Log in.',
        }
        return response_object, 409


def get_all_intitutes():
    return Institute.query.all()


def get_an_institute(id):
    return Institute.query.filter_by(id = id).first()

def delete_an_institute(id):
    institute = Institute.query.filter_by(id = id).first()
    db.session.delete(institute)
    db.session.commit()    

def update_an_institute(id):
    institute = Institute.query.filter_by(id = id).first()
    institute.name = 'Elrick'
    institute.email = 'Vera@icloud.com'    
    db.session.commit()
    return institute

  
def generate_token(user):
    try:
        # generate the auth token
        auth_token = Institute.encode_auth_token(user.id)
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

