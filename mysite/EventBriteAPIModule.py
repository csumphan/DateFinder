import urllib.request         # urllib.request.urlopen(url)
import urllib.parse           # urllib.parse.urlencode((parameter, value))
import json
from pprint import pprint

TOKEN = '77GNIJFPL3PU4ASPFJV5'
BASE_URL = 'https://www.eventbriteapi.com/v3/events/search/?'

def build_url(search_query: str, sort_by: str, location_address: str, location_within: str, price: str) -> str:
    
    parameters = urllib.parse.urlencode([('token', TOKEN),('q', search_query),('sort_by', sort_by), ('location.address', location_address), ('location.within', location_within), ('price', price)])
    return BASE_URL + parameters

def get_dict_from_json(url: str) -> dict:
    response = None
    try:
        response = urllib.request.urlopen(url)
        return json.loads(response.read().decode(encoding = 'utf-8'))
    finally:
        if response != None:
            response.close()
            
def parse(json_text: 'json text') -> list:
    result_list = []
    for event in range(len(json_text['events'])):
        try:
            result_list.append(json_text['events'][event]['name']['text']) # can return 'text' or 'html'
        except:
            pass
    return result_list
    

# Test
test = parse(get_dict_from_json(build_url('concert', 'date', 'Irvine', '10mi', 'free')))
for event in test:
    print(event)