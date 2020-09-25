from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {                
		'first_name': fields.String(required=True, description='user first_name'),
        'middle_name': fields.String(required=True, description='user middle_name'),
		'last_name': fields.String(required=True, description='user last_name'),
        'type_doc': fields.Integer(required=True, description='user type_doc'),
		'num_doc': fields.String(required=True, description='user num_doc'),
        'id_country': fields.Integer(required=True, description='user id_country'),
		'id_state': fields.Integer(required=True, description='user id_state'),
        'id_city': fields.Integer(required=True, description='user id_city'),
		'registered_on': fields.DateTime(required=True, description='user registered_on'),
        'sex': fields.String(required=True, description = 'user sex'),
        'phone': fields.String(required=False, description = 'user phone'),
        'date_birth': fields.DateTime(required=True, description='user date_birth')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password ')
    })
class AccountDto:
    api = Namespace('account', description='account related operations')
    account = api.model('account', {
        'id_user': fields.Integer(required=True, description='account id_user'),
        'id_institute': fields.Integer(required=True, description='account id_institute'),
        'email': fields.String(required=True, description='account email'),
        'password': fields.String(required=True, description='account password'),		
        'old_password': fields.String(required=False, description='account old_password'),
		'wrong_login_attempt': fields.Integer(required=True, description='account wrong_login_attempt'),
        'today_login_attempt': fields.String(required=True, description='account today_login_attempt'),
		'is_now_login': fields.Integer(required=True, description='account is_now_login'),        
		'registered_on': fields.DateTime(required=True, description='account registered_on')
    })   

class InstituteDto:
    api = Namespace('institute', description='institute related operations')
    institute = api.model('institute', {
        'name': fields.String(required=True, description='institute name'),        
        'email': fields.String(required=True, description='institute email'),
        'phone': fields.String(required=True, description='institute phone'),
        'id_country': fields.Integer(required=True, description='institute id_country'),
        'id_city': fields.Integer(required=True, description='institute id_city'),
		'id_state': fields.Integer(required=True, description='institute id_state'),        
		'registered_on': fields.DateTime(required=True, description='institute registered_on')            
    })   
class Type_docDto:
    api = Namespace('type_doc', description='type_doc related operations')
    type_doc = api.model('type_doc', {
        'short_name': fields.String(required=True, description='type_doc short_name'),        
        'name': fields.String(required=True, description='type_doc name'),
        'description': fields.String(required=True, description='type_doc description')
    })   
class Type_accDto:
    api = Namespace('type_acc', description='type_acc related operations')
    type_acc = api.model('type_acc', {        
        'name': fields.String(required=True, description='type_acc name'),
        'description': fields.String(required=True, description='type_acc description')
    })       
class Level_Dto:
    api = Namespace('level', description='level related operations')
    level = api.model('level', {        
        'name': fields.String(required=True, description='level name'),
        'description': fields.String(required=True, description='level description')
    })   
class Achievement_Dto:
    api = Namespace('achievement', description='achievement related operations')
    achievement = api.model('achievement', {
        'short_name': fields.String(required=True, description='achievement short_name'),        
        'name': fields.String(required=True, description='achievement name'),
        'description': fields.String(required=True, description='achievement description')
    })   

class Area_Dto:
    api = Namespace('area', description='area related operations')
    area = api.model('area', {
        'short_name': fields.String(required=True, description='area short_name'),        
        'name': fields.String(required=True, description='area name'),
        'description': fields.String(required=True, description='area description')
    })       

class Subject_Dto:
    api = Namespace('subject', description='subject related operations')
    subject = api.model('subject', {
        'id_area': fields.Integer(required=True, description='subject id_area'),
        'short_name': fields.String(required=True, description='subject short_name'),        
        'name': fields.String(required=True, description='subject name')        
    })       

class Achievement_trans_Dto:
    api = Namespace('achievement_trans', description='achievement_trans related operations')
    achievement_trans = api.model('achievement_trans', {
        'id_achievement': fields.Integer(required=True, description='achievement_trans id_achievement'),
        'id_account': fields.Integer(required=True, description='achievement_trans id_account'),
        'registered_on': fields.DateTime(required=True, description='achievement_trans registered_on')
    })       
