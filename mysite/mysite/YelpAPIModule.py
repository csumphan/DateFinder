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


def get_results(location: str, term: str) -> list:
    results = []
    client = Client(auth)
    params = {'term': term}
    
    response = client.search(location, **params)
    
    for b in range(len(response.businesses)):
        results.append({'name': response.businesses[b].name, 'address': response.businesses[b].location.display_address, 'rating': response.businesses[b].rating, 'image_url': response.businesses[b].image_url})

    return results


# Test
print(get_results('Irvine', 'sushi'))
