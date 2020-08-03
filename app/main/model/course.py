
from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt

class Course(db.Model):
	""" Course Model for storing course related details """
	__tablename__ = "course"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	id_student = db.Column(db.Integer, nullable=False)
	id_school_subsjects = db.Column(db.Integer, nullable=False)	
	course_name = db.Column(db.String(30), default='', nullable=False)	
	final_note =db.Column(db.DECIMAL(4,2), default=0.00 ,nullable=False)
	description = db.Column(db.String(200), default='', nullable=False)	
	registered_on = db.Column(db.DateTime, nullable=False)

	"""	
	@property
	def password(self):
		raise AttributeError('password: write-only field')
	
	@password.setter
	def password(self, password):
		self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')
		
	def check_password(self, password):
		return flask_bcrypt.check_password_hash(self.password_hash, password)
	"""
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
		return "<Course '{}'>".format(self.course_name)
