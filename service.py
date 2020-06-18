# -*- coding: utf-8 -*-
from flask import render_template #solo para pruebas
from flask import Flask, request, redirect, url_for, session, jsonify, make_response, current_app
from flask_pymongo import PyMongo
from flask_cors import CORS


from datetime import timedelta  
import bcrypt
from time import gmtime, strftime
from functools import update_wrapper
import os
from hashlib import sha512
from werkzeug.utils import secure_filename
import json
import generaldao as gdao


app = Flask(__name__)
CORS(app)


#app.config['MONGO_URI'] = 'mongodb+srv://dbUser:testting123@clustertest-etk84.mongodb.net/Ninak?retryWrites=true&w=majority'
#mongo = PyMongo(app)


#metodo para aceptar el protocolo https
def crossdomain(origin=None, methods=None, headers=None, max_age=21600, attach_to_all=True, automatic_options=True):  
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


@app.route('/login', methods = ['POST'])
def logins():
    content = request.get_json()
    username = content['username']
    password = sha512(content['password']).hexdigest()
    login = gdao.login(session['username'],password)
    return login


@app.route('/closeSession',methods=['GET'])
def close():
    session.clear()
    return '<h1> Se cerro la session ! </h1>'

if __name__ == '__main__':
    #app.secret_key = 'mysecret'
    app.run(host = '0.0.0.0', debug = True)