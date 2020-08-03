import uuid
import datetime

from app.main import db
from app.main.model.teacher import Teacher


def save_new_teacher(data):
    teacher = Teacher.query.filter_by(email=data['email']).first()
    if not teacher:
        new_teacher = Teacher(            
            id_user=data['id_user'],     
            email=data['email'],   
            registered_on=datetime.datetime.utcnow()
        )        
        save_changes(new_teacher)
        return generate_token(new_teacher)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Teacher already exists. Please Log in.',
        }
        return response_object, 409
        
def get_all_teachers():
    return Teacher.query.all()


def get_a_teacher(email):
    return Teacher.query.filter_by(email=email).first()

def delete_a_teacher(email):
    teacher = Teacher.query.filter_by(email=email).first()
    db.session.delete(teacher)
    db.session.commit()    

def update_a_teacher(email):
    teacher = Teacher.query.filter_by(email=email).first()
    teacher.email = 'huntercvd@gmail.com'
    db.session.commit()
    return teacher


def generate_token(teacher):
    try:
        # generate the auth token
        auth_token = Teacher.encode_auth_token(teacher.id)
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

