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
		'registered_on': fields.DateTime(required=True, description='user registered_on')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
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

class CourseDto:
    api = Namespace('course', description='course related operations')
    course = api.model('course', {        
        'id_student': fields.Integer(required=True, description='course id_student'),
        'id_school_subsjects': fields.Integer(required=True, description='course id_school_subsjects'),
        'course_name': fields.String(required=True, description='course course_name'),
        'final_note': fields.String(required=True, description='course final_note'),
        'description': fields.String(required=False, description='course description'),		
		'registered_on': fields.DateTime(required=True, description='course registered_on')
    })   
class TeacherDto:
    api = Namespace('teacher', description='teacher related operations')
    teacher = api.model('teacher', {        
        'id_user': fields.Integer(required=True, description='teacher id_user'),        
        'email': fields.String(required=True, description='teacher email'),                
		'registered_on': fields.DateTime(required=True, description='teacher registered_on')
    })   

