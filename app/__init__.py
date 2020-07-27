from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Ninak API',
          version='1.0',
          description='Servicios de Ninak para la plataforma streaming educativo plurilingue'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)