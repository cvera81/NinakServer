from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import InstituteDto
from ..service.institute_service import save_new_institute, get_all_intitutes, get_an_institute, delete_an_institute,update_an_institute

api = InstituteDto.api
_institute = InstituteDto.institute


@api.route('/')
class InstituteList(Resource):
    @api.doc('list_of_registered_institutes')    
    @api.marshal_list_with(_institute, envelope='data')
    def get(self):
        """List all registered institutes"""
        return get_all_intitutes()

    @api.expect(_institute, validate=True)
    @api.response(201, 'Institute successfully created.')
    @api.doc('create a new Institute')
    def post(self):
        """Creates a new Institute """
        data = request.json
        return save_new_institute(data=data)        
    

@api.route('/<id>')
@api.param('id', 'The institute identifier')
@api.response(404, 'Institute not found.')
class Institute(Resource):
    @api.doc('get an institute')
    @api.marshal_with(_institute)
    def get(self, id):
        """get a institute given its identifier"""
        institute = get_an_institute(id)
        if not institute:
            api.abort(404)
        else:
            return institute
    
    # para documentar.        
    @api.doc('delete an institute')
    @api.marshal_with(_institute)        
    def delete(self,id):
        """delete a institute given its identifier"""
        delete_an_institute(id)
        
    @api.doc('update an institute')
    @api.marshal_with(_institute)        
    def put(self,id):
        """update a institute given its identifier"""
        institute = update_an_institute(id)
        if not institute:
            api.abort(404)
        else:
            return institute        
        
        



