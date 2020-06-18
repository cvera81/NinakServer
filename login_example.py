from flask import Flask, render_template, url_for, request, session, redirect, jsonify
from flask_pymongo import PyMongo
#from .extensions import PyMongo
import bcrypt

app = Flask(__name__)

#app.config['MONGO_DBNAME'] = 'mongologinexample'
app.config['MONGO_URI'] = 'mongodb+srv://dbUser:testting123@clustertest-etk84.mongodb.net/Ninak?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        hashpass = request.form['pass'] #bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
        #print(hashpass)
        #print(login_user['password'])
        #print(login_user['password'].decode())
        if hashpass == login_user['password']:
        #if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')).decode() == login_user['password'].encode('utf-8'):
        #if bcrypt.hashpw(request.form['pass'].encode('utf-8'), bytes(bcrypt.gensalt())) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = request.form['pass'] #bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            #print(request.form['pass'].encode('utf-8'))
            #print(hashpass)
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')

@app.route('/add',methods=['GET'])
def adduser():
    user_collection = mongo.db.users
    user_collection.insert({'name':'Piero','password':'pass123'})        
    user_collection.insert({'name':'Pepito','password':'pass124'})
    user_collection.insert({'name':'Carlos','password':'pass125'})
    user_collection.insert({'name':'Alfred','password':'pass126'})

    '''
    user_collection.insert({'name':'Piero','lastname':'Vargas'})        
    user_collection.insert({'name':'Pepito','lastname':'Salas'})
    user_collection.insert({'name':'Carlos','lastname':'Buenchico'})
    user_collection.insert({'name':'Alfred','lastname':'Garcia'})
    '''
    return '<h1> Added a User! </h1>'

@app.route('/list', methods=['GET'])
def lista():
    user_collection = mongo.db.users
    listado = []
    for i in user_collection.find():
        #listado.append({'name':i['name']})
        listado.append({'name':i['name'],'password':i['password']})
    return  jsonify({'result': listado})  
@app.route('/CloseSession',methods=['GET'])
def close():
    session.clear()
    return '<h1> Se cerro la session ! </h1>'

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)