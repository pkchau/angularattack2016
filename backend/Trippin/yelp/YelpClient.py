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
            'category_filter' : ','.join(categories)
                }
        result = self.client.search(location, **params)
        return result

    def getByYelpId(self, yelp_id):
        result = self.client.get_business(yelp_id)
        return self.formatBusiness(result.business)


    def getCategory(self, location, category):
        result = self.search(location, [category])
        return self.getFormattedBusinesses(result.businesses) 

    def getActive(self, location):
        return self.getCategory(location, 'active')

    def getArts(self, location):
        return self.getCategory(location, 'arts')

    def getFood(self, location):
        return self.getCategory(location, 'food')

    def getHotels(self, location):
        return self.getCategory(location, 'hotelstravel')

    def getLocalFlavor(self, location):
        return self.getCategory(location, 'localflavor')

    def getNightLife(self, location):
        return self.getCategory(location, 'nightlife')

    def getRestaurants(self, location):
        return self.getCategory(location, 'restaurants')

    def getFormattedBusinesses(self, businesses):
        return list(map(lambda x : self.formatBusiness(x),
                         filter(lambda x : not x.is_closed, 
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
                'name' : name,
                'yelp_id' : business.id,
                'picture' : picture,
                'rating' : rating,
                'address' : address,
                'phone' : phone,
                'categories' : business.categories
                }

        return data
        

 


