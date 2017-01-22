import urllib.request         # urllib.request.urlopen(url)
import urllib.parse           # urllib.parse.urlencode((parameter, value))
import json
from pprint import pprint

API_KEY = 'AIzaSyCQqP9yDRaKDriBcU0lYHxDJ6OW5esY7Yk'
BASE_URL = 'https://maps.googleapis.com/maps/api/place/autocomplete/json?language=en&offset=3&'
TEST_INPUT = 'mis'

# api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}

def build_autocom_url(subtext) -> str:
    
    parameters = urllib.parse.urlencode([('input', subtext), ('key', API_KEY)])
    return BASE_URL + parameters

def get_dict_from_json(url: str) -> dict:
    response = None
    try:
        response = urllib.request.urlopen(url)
        return json.loads(response.read().decode(encoding = 'utf-8'))
    finally:
        if response != None:
            response.close()
            
def get_locations(json_text: 'json text') -> list:
    location_list = []
    
    for predictions in range(len(json_text['predictions'])):
        location_list.append(json_text['predictions'][predictions]['description'])
        
    return location_list  
          

#Test:
print(build_autocom_url(TEST_INPUT))
pprint(get_dict_from_json(build_autocom_url(TEST_INPUT)))
print()
print(get_locations(get_dict_from_json(build_autocom_url(TEST_INPUT))))

    
    
    


