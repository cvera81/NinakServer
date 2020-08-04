from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import StudentDto
from ..service.student_service import save_new_student, get_all_students, get_a_student, delete_a_student,update_a_student

api = StudentDto.api
_student = StudentDto.student


@api.route('/')
class StudentList(Resource):
    @api.doc('list_of_registered_students')    
    @api.marshal_list_with(_student, envelope='data')
    def get(self):
        """List all registered students"""
        return get_all_students()

    @api.expect(_student, validate=True)
    @api.response(201, 'Student successfully created.')
    @api.doc('create a new Student')
    def post(self):
        """Creates a new Student """
        data = request.json
        return save_new_student(data=data)        
    

@api.route('/<id>')
@api.param('id', 'The student identifier')
@api.response(404, 'Student not found.')
class Student(Resource):
    @api.doc('get an student')
    @api.marshal_with(_student)
    def get(self, id):
        """get a student given its identifier"""
        student = get_a_student(id)
        if not student:
            api.abort(404)
        else:
            return student
    
    # para documentar.        
    @api.doc('delete a student')
    @api.marshal_with(_student)        
    def delete(self,id):
        """delete a student given its identifier"""
        delete_a_student(id)
        
    @api.doc('update a student')
    @api.marshal_with(_student)        
    def put(self,id):
        """update a student given its identifier"""
        student = update_a_student(id)
        if not student:
            api.abort(404)
        else:
            return student        
        
        



