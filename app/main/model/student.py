
from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt

class Student(db.Model):
	""" Student Model for storing teacher related details """
	__tablename__ = "student"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	id_account = db.Column(db.Integer, nullable=False)	
	student_code = db.Column(db.String(30),  nullable=False)
	registered_on = db.Column(db.DateTime, nullable=False)


	@staticmethod
	def encode_auth_token(id):
		"""
		Generates the Auth Token
		:return: string
		"""
		try:
			payload = {
				'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
				'iat': datetime.datetime.utcnow(),
				'sub': id
			}
			return jwt.encode(
				payload,
				key,
				algorithm='HS256'
			)
		except Exception as e:
			return e
	
	@staticmethod
	def decode_auth_token(auth_token):
		"""
		Decodes the auth token
		:param auth_token:
		:return: integer|string
		"""
		try:
			payload = jwt.decode(auth_token, key)
			is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
			if is_blacklisted_token:
				return 'Token blacklisted. Please log in again.'
			else:
				return payload['sub']
		except jwt.ExpiredSignatureError:
			return 'Signature expired. Please log in again.'
		except jwt.InvalidTokenError:
			return 'Invalid token. Please log in again.'
	
	def __repr__(self):
		return "<Teacher '{}'>".format(self.id)