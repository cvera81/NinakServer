from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import Achievement_Dto
from ..service.achievement_service import save_new_achievement, get_all_achievements, get_an_achievement, delete_an_achievement,update_an_achievement

api = Achievement_Dto.api
_achievement = Achievement_Dto.achievement


@api.route('/')
class Achievement_List(Resource):
    @api.doc('list_of_registered_achievements')
    #@admin_token_required
    @api.marshal_list_with(_achievement, envelope='data')
    def get(self):
        """List all registered achivements"""
        return get_all_achievements()

    @api.expect(_achievement, validate=True)
    @api.response(201, 'Achievement successfully created.')
    @api.doc('create a new Achievement')
    def post(self):
        """Creates a new Achievement """
        data = request.json
        return save_new_achievement(data=data)

    @api.expect(_achievement, validate=True)
    @api.response(201, 'Achievement successfully updated.')
    @api.doc('Update an Achievement')
    def put(self):
        data = request.json
        return update_an_achievement(data)

@api.route('/<short_name>')
@api.param('short_name', 'The _achievement identifier')
@api.response(404, 'achievement not found.')
class Achievement(Resource):
    @api.doc('get an achievement')
    @api.marshal_with(_achievement)
    def get(self, short_name):
        """get a achievement given its identifier"""
        achievement = get_an_achivement(short_name)
        if not achievement:
            api.abort(404)
        else:
            return achievement

    @api.doc('delete a achievement')
    @api.marshal_with(_achievement)        
    def delete(self,short_name):
        """delete a achievement given its identifier"""
        delete_an_achievement(short_name)
        



