import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(num_doc=data['num_doc']).first()
    if not user:
        new_user = User(        
			first_name = data['first_name'],
			middle_name = data['middle_name'],
			last_name = data['last_name'],
			type_doc = data['type_doc'],
			num_doc = data['num_doc'],
			id_country = data['id_country'],
			id_state = data['id_state'],
			id_city = data['id_city'],
            registered_on = datetime.datetime.utcnow(),
            sex = data['sex'],
            phone = data['phone'],
            date_birth = datetime.datetime.utcnow() #data['date_birth']
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_an_user(num_doc):
    return User.query.filter_by(num_doc = num_doc).first()

def delete_an_user(num_doc):
    return User.query.filter_by(num_doc = num_doc).delete()    


def update_an_user(data):
	user = User.query.filter_by(num_doc = data['num_doc']).first()
	user.first_name = data['first_name']    
    #user.middle_name = data['middle_name']
    #user.last_name = data['last_name']
    #user.sex = data['sex']
    #user.phone = data['phone']  
    #user.date_birh = data['date_birh']
    
	db.session.commit()
	return 201    

def generate_token(user):
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(user.id)
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

