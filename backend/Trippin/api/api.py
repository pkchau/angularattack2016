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
        return jsonify({'user_id':foundUser.user_id,'email':foundUser.email,'first_name':foundUser.first_name,'last_name':foundUser.last_name})
    
    newUser=User(email=request.get_json().get('email'),first_name=request.get_json().get('first_name'),last_name=request.get_json().get('last_name'))
    db.session.add(newUser)
    db.session.commit()
    newUser=find_user(newUser.email)
    return jsonify({'user_id':newUser.user_id,'email':newUser.email,'first_name':newUser.first_name,'last_name':newUser.last_name})

#handle trip information
@app.route('/trip_query',methods=['POST'])
def trip_query():
    numResults=int(request.get_json().get('numResults'))
    location=request.get_json().get('location')
    yelpCategories=request.get_json().get('yelp_categories').split(',')
    yelpLookup=YC.YelpClient()
    return jsonify({'output':yelpLookup.getCategory(numResults,location,yelpCategories)})


#save trip information

        



