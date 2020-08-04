import uuid
import datetime

from app.main import db
from app.main.model.account import Account


def save_new_account(data):
    account = Account.query.filter_by(email=data['email']).first()
    if not account:
        new_account = Account(
            id_user=data['id_user'],
            id_institute=data['id_institute'],
            email=data['email'],
            password_hash=data['password_hash'],											            
			old_password=data['old_password'],
			wrong_login_attempt=data['wrong_login_attempt'],
			today_login_attempt=data['today_login_attempt'],
			is_now_login=data['is_now_login'],
            registered_on=datetime.datetime.utcnow()
        )        
        save_changes(new_account)
        return generate_token(new_account)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Account already exists. Please Log in.',
        }
        return response_object, 409


def get_all_accounts():
    return Account.query.all()


def get_an_account(email):
    return Account.query.filter_by(email = email).first()


def delete_an_account(email):
    account = Account.query.filter_by(email = email).first()
    db.session.delete(account)
    db.session.commit()    

def update_an_account(email):
    account = Account.query.filter_by(email = email).first()
    account.email = 'cvera@geeksonsite.com'        
    db.session.commit()
    return account

def generate_token(account):
    try:
        # generate the auth token
        auth_token = Account.encode_auth_token(account.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()

