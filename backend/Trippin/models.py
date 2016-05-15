from Trippin import db
class User(db.Model): 
    __tablename__="users"
    user_id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(255), index=True, unique=True)
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))
    def is_active(self):
        return True
    def is_anonymous(self): 
        return False
    def is_authenticated(self):
        return True
    def get_id(self): 
        return str(self.user_id)
    
class Trip(db.Model): 
    __tablename__="trips"
    trip_id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,index=True)
    location=db.Column(db.String(255))
    startDate=db.Column(db.DateTime)
    endDate=db.Column(db.DateTime)

