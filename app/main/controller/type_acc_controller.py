from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import Type_accDto
from ..service.type_acc_service import save_new_type_acc, get_all_type_accs, get_a_type_acc,delete_a_type_acc,update_a_type_acc

api = Type_accDto.api
_type_acc = Type_accDto.type_acc


@api.route('/')
class Type_accList(Resource):
    @api.doc('list_of_registered_type_accs')
    #@admin_token_required
    @api.marshal_list_with(_type_acc, envelope='data')
    def get(self):
        """List all registered type_accs"""
        return get_all_type_accs()

    @api.expect(_type_acc, validate=True)
    @api.response(201, 'Type_acc successfully created.')
    @api.doc('create a new Type_acc')
    def post(self):
        """Creates a new Type_acc """
        data = request.json
        return save_new_type_acc(data=data)

    @api.expect(_type_acc, validate=True)
    @api.response(201, 'Type_acc successfully updated.')
    @api.doc('Update an type_acc')
    def put(self):
        data = request.json
        return update_a_type_acc(data)

@api.route('/<name>')
@api.param('name', 'The type_acc identifier')
@api.response(404, 'type_acc not found.')
class Type_doc(Resource):
    @api.doc('get a type_acc')
    @api.marshal_with(_type_acc)
    def get(self, name):
        """get a type_acc given its identifier"""
        type_acc = get_a_type_acc(name)
        if not type_acc:
            api.abort(404)
        else:
            return type_acc

    @api.doc('delete a type_acc')
    @api.marshal_with(_type_acc)        
    def delete(self,name):
        """delete a type_acc given its identifier"""
        delete_a_type_acc(name)
        



