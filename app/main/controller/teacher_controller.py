from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import TeacherDto
from ..service.teacher_service import save_new_teacher, get_all_teachers, get_a_teacher, delete_a_teacher,update_a_teacher

api = TeacherDto.api
_teacher = TeacherDto.teacher


@api.route('/')
class TeacherList(Resource):
    @api.doc('list_of_registered_teachers')    
    @api.marshal_list_with(_teacher, envelope='data')
    def get(self):
        """List all registered teachers"""
        return get_all_teachers()

    @api.expect(_teacher, validate=True)
    @api.response(201, 'Teacher successfully created.')
    @api.doc('create a new teacher')
    def post(self):
        """Creates a new Teacher """
        data = request.json
        return save_new_teacher(data=data)        
    

@api.route('/<email>')
@api.param('email', 'The teacher identifier')
@api.response(404, 'Teacher not found.')
class Teacher(Resource):
    @api.doc('get an teacher')
    @api.marshal_with(_teacher)
    def get(self, email):
        """get a teacher given its identifier"""
        teacher = get_a_teacher(email)
        if not teacher:
            api.abort(404)
        else:
            return teacher
    
    # para documentar.        
    @api.doc('delete a teacher')
    @api.marshal_with(_teacher)        
    def delete(self,email):
        """delete a teacher given its identifier"""
        delete_a_teacher(email)
        
    @api.doc('update a teacher')
    @api.marshal_with(_teacher)        
    def put(self,email):
        """update a teacher given its identifier"""
        teacher = update_a_teacher(email)
        if not teacher:
            api.abort(404)
        else:
            return teacher        
        
        



