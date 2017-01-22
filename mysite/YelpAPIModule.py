from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

CONSUMER_KEY = '_bCThVChD7K7sjwx7HLgFQ'
CONSUMER_SECRET = 'ZP8JJEYkq7E8ZEEq8jaFBPm27XM'
TOKEN = 'xyMTBVlt13pkFFRQ_gdk1zROcmmb_h1K'
TOKEN_SECRET = 'w96ZZMxUdx7tmvg3Ntv17CxMg2k'

auth = Oauth1Authenticator(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    token=TOKEN,
    token_secret=TOKEN_SECRET
)

client = Client(auth)

params = {
    'term': 'sushi',
}


# Test
response = client.search('Irvine', **params)

for b in range(len(response.businesses)):
    print(response.businesses[b].name)
    print(response.businesses[b].location.address)
    print()
