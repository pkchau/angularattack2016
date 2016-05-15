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

    def search(self, offset, location,categories):
        params = {
            'category_filter' : ','.join(categories),
            'offset' : offset,
            }
        result = self.client.search(location, **params)
        return result

    def getByYelpId(self, yelp_id):
        result = self.client.get_business(yelp_id)
        return self.formatBusinesses(result.business)


    def getCategory(self,numResults, location, category):
        offset=0
        outList=[]
        while numResults>0:
            numResults-=20
            offset+=20
            result = self.search(offset, location, category)
            self.getFormattedBusinesses(result.businesses,outList)
        return outList

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

    def getFormattedBusinesses(self, businesses,outList):
        return list(map(lambda x : outList.append(self.formatBusiness(x)),
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
        source = 'yelp'
        
        data = {
                'name' : name,
                'external_id' : yelp_id,
                'picture' : picture,
                'rating' : rating,
                'address' : address,
                'phone' : phone,
                'source': source,
                'categories' : business.categories
                }

        return data
        

 


