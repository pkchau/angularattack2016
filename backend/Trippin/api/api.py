import json
from flask import jsonify, request,session,g
from flask.ext.login import login_required,login_user, logout_user,current_user
from Trippin import app,models,login_manager,db
from Trippin.yelp import YelpClient as YC 


User=models.User

def find_user(userEmail): 
    userCheck=User.query.filter_by(email=userEmail).first()
    db.session.commit()
    return userCheck

#main page
@app.route('/')
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
    foundUser=find_user(request.get_json().get('email'))
    if foundUser is not None:    
        return jsonify({'user_id':foundUser.user_id})
    
    newUser=User(email=request.get_json().get('email'),first_name=request.get_json().get('first_name'),last_name=request.get_json().get('last_name'))
    db.session.add(newUser)
    db.session.commit()
    userId=find_user(newUser.email).user_id
    return jsonify({'user_id':userId})

#handle trip information
@app.route('/trip_query',methods=['POST'])
def trip_maker():
    location=request.get_json().get('location')
    yelpCategories=request.get_json().get('yelp_categories')
    
    yelpLookup=YC.YelpClient()
    foundEvents=[]
    for category in list(yelpCategories):
            map(lambda x: foundEvents.append(x))
