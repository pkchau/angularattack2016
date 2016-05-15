import json
from flask import jsonify, request,session,g

from flask.ext.login import login_required,login_user, logout_user,current_user

from Trippin import app,models,login_manager,db
User=models.User

def find_user(user): 
    userCheck=User.query.filter_by(email=user).first()
    db.session.commit()
    return userCheck

#main page
@app.route('/')
@login_required
def home():
    return jsonifiy({'status':'what are you doing here'})


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

@app.before_request
def before_request(): 
    g.user=current_user


#handle registration
@app.route('/register',methods=['POST'])
def register(): 
    if find_user(request.get_json().get('email')) is not None:
        return jsonify({'status':'already registered'})
    newUser=User(email=request.get_json().get('email'),first_name=request.get_json().get('first_name'),last_name=request.get_json().get('last_name'))
    db.session.add(newUser)
    db.session.commit()

    return jsonify({'status':'registered'})


