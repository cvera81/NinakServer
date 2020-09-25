
from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt

class Achievement_trans(db.Model):
	""" achievement_trans Model for storing achievement_trans related details """
	__tablename__ = "achievement_trans"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)	
	id_achievement = db.Column(db.Integer, default=0, nullable=False)
	id_account = db.Column(db.Integer, default=0, nullable=False)
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
		return "<Achievement_trans '{}'>".format(self.id_achievement)
