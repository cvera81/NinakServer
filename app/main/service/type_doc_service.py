import uuid
import datetime

from app.main import db
from app.main.model.type_doc import Type_doc


def save_new_type_doc(data):
    type_doc = Type_doc.query.filter_by(short_name=data['short_name']).first()
    if not type_doc:
        new_type_doc = Type_doc(        
			short_name = data['short_name'],
			name = data['name'],
			description = data['description']
        )
        save_changes(new_type_doc)
        return generate_token(new_type_doc)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Type_doc already exists. Please insert another.',
        }
        return response_object, 409


def get_all_type_docs():
    return Type_doc.query.all()


def get_a_type_doc(short_name):
    return Type_doc.query.filter_by(short_name = short_name).first()

def delete_a_type_doc(short_name):
    return Type_doc.query.filter_by(short_name = short_name).delete()    


def update_a_type_doc(data):
    type_doc = Type_doc.query.filter_by(short_name = data['short_name']).first()
    type_doc.name=data['name']
    db.session.commit()
    return 201    

def generate_token(type_doc):
    try:
        # generate the auth token
        auth_token = Type_doc.encode_auth_token(type_doc.id)
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

