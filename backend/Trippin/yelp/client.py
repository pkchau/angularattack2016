from Trippin import config

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key=config.YELP_KEYS['consumer_key'],
    consumer_secret=config.YELP_KEYS['consumer_secret'],
    token=config.YELP_KEYS['token'],
    token_secret=config.YELP_KEYS['token_secret'],
)

client = Client(auth)

