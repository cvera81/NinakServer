import uuid
import datetime

from app.main import db
from app.main.model.course import Course


def save_new_course(data):
    course = Course.query.filter_by(id=data['id']).first()
    if not course:
        new_course = Course(                                    
            name=data['name'],            
			description=data['description'],			            
        )        
        save_changes(new_course)
        return generate_token(new_course)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Account already exists. Please Log in.',
        }
        return response_object, 409


def get_all_courses():
    return Course.query.all()


def get_a_course(id):
    return Course.query.filter_by(id = id).first()

def delete_a_course(id):
    course = Course.query.filter_by(id = id).first()
    db.session.delete(course)
    db.session.commit()    

def update_a_course(id):
    course = Course.query.filter_by(id = id).first()
    course.name = 'new course'
    course.description = 'curso recomendado'
    db.session.commit()
    return course



def generate_token(course):
    try:
        # generate the auth token
        auth_token = Course.encode_auth_token(course.id)
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

