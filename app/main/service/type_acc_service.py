import uuid
import datetime

from app.main import db

from app.main.model.type_acc import Type_acc

def save_new_type_acc(data):
    type_acc = Type_acc.query.filter_by(name = data['name']).first()
    if not type_acc:
        new_type_acc = Type_acc(        			
			name = data['name'],
			description = data['description']
        )
        save_changes(new_type_acc)
        return generate_token(new_type_acc)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Type_acc already exists. Please insert another.',
        }
        return response_object, 409


def get_all_type_accs():
    return Type_acc.query.all()


def get_a_type_acc(name):
    return Type_acc.query.filter_by(name = name).first()

def delete_a_type_acc(name):
    return Type_acc.query.filter_by(name = name).delete()    


def update_a_type_acc(data):
    type_acc = Type_acc.query.filter_by(name = data['name']).first()
    type_acc.description = data['description']
    db.session.commit()
    return 201    

def generate_token(type_acc):
    try:
        # generate the auth token
        auth_token = Type_acc.encode_auth_token(type_acc.id)
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

