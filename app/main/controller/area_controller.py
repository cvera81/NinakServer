from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import Area_Dto
from ..service.area_service import save_new_area, get_all_areas, get_an_area, delete_an_area,update_an_area

api = Area_Dto.api
_area = Area_Dto.area


@api.route('/')
class Area_List(Resource):
    @api.doc('list_of_registered_areas')
    #@admin_token_required
    @api.marshal_list_with(_area, envelope='data')
    def get(self):
        """List all registered areas"""
        return get_all_areas()

    @api.expect(_area, validate=True)
    @api.response(201, 'Area successfully created.')
    @api.doc('create a new Area')
    def post(self):
        """Creates a new Area """
        data = request.json
        return save_new_area(data=data)

    @api.expect(_area, validate=True)
    @api.response(201, 'Area successfully updated.')
    @api.doc('Update an Area')
    def put(self):
        data = request.json
        return update_an_area(data)

@api.route('/<short_name>')
@api.param('short_name', 'The _area identifier')
@api.response(404, 'area not found.')
class Area(Resource):
    @api.doc('get an area')
    @api.marshal_with(_area)
    def get(self, short_name):
        """get a area given its identifier"""
        area = get_an_area(short_name)
        if not area:
            api.abort(404)
        else:
            return area

    @api.doc('delete a area')
    @api.marshal_with(_area)        
    def delete(self,short_name):
        """delete a area given its identifier"""
        delete_an_area(short_name)
        



