from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.account_controller import api as account_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.institute_controller import api as institute_ns
from .main.controller.type_doc_controller import api as type_doc_ns
from .main.controller.type_acc_controller import api as type_acc_ns
from .main.controller.level_controller import api as level_ns
from .main.controller.achievement_controller import api as achivement_ns
from .main.controller.area_controller import api as area_ns
from .main.controller.subject_controller import api as subject_ns
from .main.controller.achievement_trans_controller import api as achievement_trans_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Ninak API',
          version='1.0',
          description='Servicios de Ninak para la plataforma streaming educativo plurilingue'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(account_ns, path='/account')
api.add_namespace(institute_ns, path='/institute')
api.add_namespace(type_doc_ns, path='/type_doc')
api.add_namespace(type_acc_ns, path='/type_acc')
api.add_namespace(level_ns, path='/level')
api.add_namespace(achivement_ns, path='/achivement')
api.add_namespace(area_ns, path='/area')
api.add_namespace(subject_ns, path='/subject')
api.add_namespace(achievement_trans_ns, path='/achievement_trans')
