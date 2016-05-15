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
    login_user(newUser)

    return jsonify({'status':'registered'})


#handle login 
@app.route('/login', methods=["POST"])
def login(): 
    if g.user is not None and g.user.is_authenticated(): 
        logout_user()
    
    session['remember_me']=True
    foundUser=find_user(request.form['email'])
        
    if foundUser is None:
        return jsonify({'status': 'No Login'})

    login_user(foundUser,remember=True)
    return jsonify({'status':'Logged In'})


#handle log out
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return Response(jsonify({'status':'logged out'}))    
