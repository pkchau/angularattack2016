import json
from flask import jsonify, request
from flask.ext.login import LoginManager, UserMixin, login_required,login_user, logout_user


from Trippin import app

#main page
@app.route('/')
@login_required
def home():
    return Response(jsonifiy({'status':'what you doing here'}))


#handle login 
@app.route('/login', methods=["POST"])
def login(): 
    username=request.form['username']
    password=request.form['password']



#handle log out

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return Response(jsonify({'status':'logged out'}))    
