from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_an_user,delete_an_user,update_an_user

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    #@admin_token_required
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully updated.')
    @api.doc('Update an user')
    def put(self):
        data = request.json
        return update_an_user(data)

@api.route('/<num_doc>')
@api.param('num_doc', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, num_doc):
        """get a user given its identifier"""
        user = get_an_user(num_doc)
        if not user:
            api.abort(404)
        else:
            return user

    @api.doc('delete a user')
    @api.marshal_with(_user)        
    def delete(self,num_doc):
        """delete a user given its identifier"""
        delete_an_user(num_doc)
        



