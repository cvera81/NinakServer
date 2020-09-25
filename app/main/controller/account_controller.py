from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import AccountDto
from ..service.account_service import save_new_account, get_all_accounts, get_an_account,update_an_account,delete_an_account

api = AccountDto.api
_account = AccountDto.account


@api.route('/')
class AccountList(Resource):
	@api.doc('list_of_registered_accounts')
	
	@api.marshal_list_with(_account, envelope='data')
	def get(self):
		"""List all registered accounts"""
		return get_all_accounts()

	@api.expect(_account, validate=True)
	@api.response(201, 'Account successfully created.')
	@api.doc('create a new account')
	def post(self):
		"""Creates a new Account """
		data = request.json
		return save_new_account(data=data)

	@api.expect(_account, validate=True)
	@api.response(201, 'Account successfully created.')
	@api.doc('Update account')
	def put(self):
		data = request.json
		return update_an_account(data)





@api.route('/<email>')
@api.param('email', 'The Account identifier')
@api.response(404, 'Account not found.')
class Account(Resource):
	@api.doc('get an account')
	@api.marshal_with(_account)
	def get(self, email):
		"""get an account given its identifier"""
		account = get_an_account(email)
		if not account:
			api.abort(404)
		else:
			return account

	@api.doc('delete an account')
	@api.marshal_with(_account)        
	def delete(self,email):
		"""delete an account given its identifier"""
		delete_an_account(email)


