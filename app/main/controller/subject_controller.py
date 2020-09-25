from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import Subject_Dto
from ..service.subject_service import save_new_subject, get_all_subjects, get_a_subject, delete_a_subject,update_a_subject

api = Subject_Dto.api
_subject = Subject_Dto.subject


@api.route('/')
class Subject_List(Resource):
    @api.doc('list_of_registered_subjects')
    #@admin_token_required
    @api.marshal_list_with(_subject, envelope='data')
    def get(self):
        """List all registered subjects"""
        return get_all_subjects()

    @api.expect(_subject, validate=True)
    @api.response(201, 'Subject successfully created.')
    @api.doc('create a new Subject')
    def post(self):
        """Creates a new Subject """
        data = request.json
        return save_new_subject(data=data)

    @api.expect(_subject, validate=True)
    @api.response(201, 'Subject successfully updated.')
    @api.doc('Update a Subject')
    def put(self):
        data = request.json
        return update_a_subject(data)

@api.route('/<short_name>')
@api.param('short_name', 'The Subject identifier')
@api.response(404, 'subject not found.')
class Subject(Resource):
    @api.doc('get a subject')
    @api.marshal_with(_subject)
    def get(self, short_name):
        """get a subject given its identifier"""
        subject = get_a_subject(short_name)
        if not subject:
            api.abort(404)
        else:
            return subject

    @api.doc('delete a subject')
    @api.marshal_with(_subject)        
    def delete(self,short_name):
        """delete a subject given its identifier"""
        delete_a_subject(short_name)
        



