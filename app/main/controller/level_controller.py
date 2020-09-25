from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import Level_Dto
from ..service.level_service import save_new_level, get_all_levels, get_a_level,delete_a_level,update_a_level

api = Level_Dto.api
_level = Level_Dto.level


@api.route('/')
class Level_List(Resource):
    @api.doc('list_of_registered_levels')
    #@admin_token_required
    @api.marshal_list_with(_level, envelope='data')
    def get(self):
        """List all registered levels"""
        return get_all_levels()

    @api.expect(_level, validate=True)
    @api.response(201, 'Level successfully created.')
    @api.doc('create a new Level')
    def post(self):
        """Creates a new Level """
        data = request.json
        return save_new_level(data=data)

    @api.expect(_level, validate=True)
    @api.response(201, 'Level successfully updated.')
    @api.doc('Update an level')
    def put(self):
        data = request.json
        return update_a_level(data)

@api.route('/<name>')
@api.param('name', 'The level identifier')
@api.response(404, 'level not found.')
class Level_doc(Resource):
    @api.doc('get a level')
    @api.marshal_with(_level)
    def get(self, name):
        """get a level given its identifier"""
        level = get_a_level(name)
        if not level:
            api.abort(404)
        else:
            return level

    @api.doc('delete a level')
    @api.marshal_with(_level)        
    def delete(self,name):
        """delete a type_doc given its identifier"""
        delete_a_level(name)
        



