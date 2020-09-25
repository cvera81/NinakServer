from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import Type_docDto
from ..service.type_doc_service import save_new_type_doc, get_all_type_docs, get_a_type_doc,delete_a_type_doc,update_a_type_doc

api = Type_docDto.api
_type_doc = Type_docDto.type_doc


@api.route('/')
class Type_docList(Resource):
    @api.doc('list_of_registered_type_docs')
    #@admin_token_required
    @api.marshal_list_with(_type_doc, envelope='data')
    def get(self):
        """List all registered type_docs"""
        return get_all_type_docs()

    @api.expect(_type_doc, validate=True)
    @api.response(201, 'Type_doc successfully created.')
    @api.doc('create a new Type_doc')
    def post(self):
        """Creates a new Type_doc """
        data = request.json
        return save_new_type_doc(data=data)

    @api.expect(_type_doc, validate=True)
    @api.response(201, 'Type_doc successfully updated.')
    @api.doc('Update an type_doc')
    def put(self):
        data = request.json
        return update_a_type_doc(data)

@api.route('/<short_name>')
@api.param('short_name', 'The type_doc identifier')
@api.response(404, 'type_doc not found.')
class Type_doc(Resource):
    @api.doc('get a type_doc')
    @api.marshal_with(_type_doc)
    def get(self, short_name):
        """get a type_doc given its identifier"""
        type_doc = get_a_type_doc(short_name)
        if not type_doc:
            api.abort(404)
        else:
            return type_doc

    @api.doc('delete a type_doc')
    @api.marshal_with(_type_doc)        
    def delete(self,short_name):
        """delete a type_doc given its identifier"""
        delete_a_type_doc(short_name)
        



