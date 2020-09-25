from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import InstituteDto
from ..service.institute_service import save_new_Institute, get_all_institutes, get_an_institute,update_an_institute,delete_an_institute

api = InstituteDto.api
_institute = InstituteDto.institute

@api.route('/')
class InstituteList(Resource):
	@api.doc('list_of_registered_institutes')
	
	@api.marshal_list_with(_institute, envelope='data')
	def get(self):
		"""List all registered institutes"""
		return get_all_institutes()

	@api.expect(_institute, validate=True)
	@api.response(201, 'Institute successfully created.')
	@api.doc('create a new institute')
	def post(self):
		"""Creates a new Institute """
		data = request.json
		return save_new_Institute(data=data)

	@api.expect(_institute, validate=True)
	@api.response(201, 'Institute successfully created.')
	@api.doc('Update Institute')
	def put(self):
		data = request.json
		return update_an_institute(data)

@api.route('/<email>')
@api.param('email', 'The Institute identifier')
@api.response(404, 'Institute not found.')
class Institute(Resource):
	@api.doc('get an institute')
	@api.marshal_with(_institute)
	def get(self, email):
		"""get an institute given its identifier"""
		account = get_an_institute(email)
		if not account:
			api.abort(404)
		else:
			return account

	@api.doc('delete an institute')
	@api.marshal_with(_institute)        
	def delete(self,email):
		"""delete an institute given its identifier"""
		delete_an_institute	(email)


