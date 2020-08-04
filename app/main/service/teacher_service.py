import uuid
import datetime

from app.main import db
from app.main.model.teacher import Teacher


def save_new_teacher(data):
    teacher = Teacher.query.filter_by(id=data['id']).first()
    if not teacher:
        new_teacher = Teacher(            
            id_account=data['id_account'],     
            teacher_code=data['teacher_code'],   
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


def get_a_teacher(id):
    return Teacher.query.filter_by(id=id).first()

def delete_a_teacher(id):
    teacher = Teacher.query.filter_by(id=id).first()
    db.session.delete(teacher)
    db.session.commit()    

def update_a_teacher(id):
    teacher = Teacher.query.filter_by(id=id).first()
    teacher.teacher_code = '123123213132'
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

