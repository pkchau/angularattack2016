from Trippin import app

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


class YelpClient():

    def __init__(self):
        auth = Oauth1Authenticator(
            consumer_key=app.config['YELP_KEYS']['consumer_key'],
            consumer_secret=app.config['YELP_KEYS']['consumer_secret'],
            token=app.config['YELP_KEYS']['token'],
            token_secret=app.config['YELP_KEYS']['token_secret'],
        )

        self.client = Client(auth)

    def search(self, location,categories):
        params = {
            'category' : ','.join(categories)
                }
        result = self.client.search(location, **params)
        return result

    def getActive(self, location):
        result = self.search(location, ['active'])
        return getFormattedBusinesses(result.businesses) 


    def getFormattedBusinesses(self, businesses):
        return list(map(lambda x : self.formatBusiness(x),
                         filter(lambda x : not is_closed(x), 
                                businesses)))


    def formatBusiness(self, business):
        """get name,
        picture,
        cost,
        rating,
        address,"""
        yelp_id = business.id
        name = business.name
        rating = business.rating
        address = ','.join(business.location.display_address)
        phone = business.phone
        picture = business.image_url

        data = {
                'yelp_id' : business.id,
                'picture' : picture,
                'rating' : rating,
                'address' : address,
                'phone' : phone
                }

        return data
        

 


