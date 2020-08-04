from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.account_controller import api as account_ns
from .main.controller.course_controller import api as course_ns
from .main.controller.teacher_controller import api as teacher_ns
from .main.controller.student_controller import api as student_ns
from .main.controller.institute_controller import api as institute_ns

from .main.controller.auth_controller import api as auth_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Ninak API',
          version='1.0',
          description='Servicios de Ninak para la plataforma streaming educativo plurilingue'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(account_ns, path='/account')
api.add_namespace(course_ns, path='/course')
api.add_namespace(teacher_ns, path='/teacher')
api.add_namespace(student_ns, path='/student')
api.add_namespace(institute_ns, path='/institute')
"""
[ok] user acomodarlo
[ok] profesor
[ok] cursos

Nos ubicamos en main, luego ejecutamos este comando
rm ninak_dev.db
Luego vamos a la raiz principal y ubicamos la carpeta migrations, luego ejecutamos
rm -Rf migrations
ejecutamos la app
python manage.py db init
python manage.py db migrate --message "test"
python manage.py db upgrade
make run
y que se haga la magia!!!!


"""