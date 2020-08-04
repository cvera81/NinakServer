import uuid
import datetime

from app.main import db
from app.main.model.student import Student


def save_new_student(data):
    student = Student.query.filter_by(id=data['id']).first()
    if not student:
        new_student = Student(            
            id_account=data['id_account'],     
            student_code=data['student_code'],   
            registered_on=datetime.datetime.utcnow()
        )        
        save_changes(new_student)
        return generate_token(new_student)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Student already exists. Please Log in.',
        }
        return response_object, 409
        
def get_all_students():
    return Student.query.all()


def get_a_student(id):
    return Student.query.filter_by(id=id).first()

def delete_a_student(id):
    student = Student.query.filter_by(id=id).first()
    db.session.delete(student)
    db.session.commit()    

def update_a_student(id):
    student = Student.query.filter_by(id=id).first()
    student.student_code = '123123213132'
    db.session.commit()
    return student


def generate_token(teacher):
    try:
        # generate the auth token
        auth_token = Student.encode_auth_token(teacher.id)
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

