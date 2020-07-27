from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
		'first_name': fields.String(required=True, description='user first_name'),
        'middle_name': fields.String(required=True, description='user middle_name'),
		'last_name': fields.String(required=True, description='user last_name'),
        'type_doc': fields.Integer(required=True, description='user type_doc'),
		'num_doc': fields.String(required=True, description='user num_doc'),
        'id_country': fields.Integer(required=True, description='user id_country'),
		'id_state': fields.Integer(required=True, description='user id_state'),
        'id_city': fields.Integer(required=True, description='user id_city'),
		'registered_on': fields.DateTime(required=True, description='user registered_on')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
