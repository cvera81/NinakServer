from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import Achievement_trans_Dto
from ..service.achievement_trans_service import save_new_achievement_trans, get_all_achievements_trans, get_an_achievement_trans, delete_an_achievement_trans,update_an_achievement_trans

api = Achievement_trans_Dto.api
_achievement_trans = Achievement_trans_Dto.achievement_trans


@api.route('/')
class Achievement_trans_List(Resource):
    @api.doc('list_of_registered_achievements_trans')
    
    @api.marshal_list_with(_achievement_trans, envelope='data')
    def get(self):
        """List all registered achivements_trans"""
        return get_all_achievements_trans()

    @api.expect(_achievement_trans, validate=True)
    @api.response(201, 'Achievement_trans successfully created.')
    @api.doc('create a new Achievement_trans')
    def post(self):
        """Creates a new Achievement_trans """
        data = request.json
        return save_new_achievement_trans(data=data)

    @api.expect(_achievement_trans, validate=True)
    @api.response(201, 'Achievement_trans successfully updated.')
    @api.doc('Update an Achievement_trans')
    def put(self):
        data = request.json
        return update_an_achievement_trans(data)

@api.route('/<id_achievement>')
@api.param('id_achievement', 'The achievement_trans identifier')
@api.response(404, 'achievement_trans not found.')
class Achievement_trans(Resource):
    @api.doc('get an achievement_trans')
    @api.marshal_with(_achievement_trans)
    def get(self, id_achievement):
        """get a achievement_trans given its identifier"""
        achievement_trans = get_an_achievement_trans(id_achievement)
        if not achievement_trans:
            api.abort(404)
        else:
            return achievement_trans

    @api.doc('delete a achievement_trans')
    @api.marshal_with(_achievement_trans)        
    def delete(self,id_achievement):
        """delete a achievement_trans given its identifier"""
        delete_an_achievement_trans(id_achievement)
        



