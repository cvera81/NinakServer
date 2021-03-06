
from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt

class Institute(db.Model):
	""" Institute Model for storing user related details """
	__tablename__ = "institute"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)	
	name = db.Column(db.String(30), default='', nullable=False)
	email = db.Column(db.String(30), unique=True, nullable=False)
	phone = db.Column(db.String(30), default='', nullable=False)
	id_country = db.Column(db.Integer, nullable=False)
	id_city = db.Column(db.Integer, nullable=False)
	id_state = db.Column(db.Integer, nullable=False)	
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
		return "<Institute '{}'>".format(self.name)
