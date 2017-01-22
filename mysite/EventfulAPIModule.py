import urllib.request         # urllib.request.urlopen(url)
import urllib.parse           # urllib.parse.urlencode((parameter, value))
import json



KEY = 'WcHjThBZW5Kmd66V'
BASE_URL = 'http://api.eventful.com/json/events/search?'

def build_url(location: str) -> str:
    
    parameters = urllib.parse.urlencode([('app_key', KEY), ('location', location)])
    return BASE_URL + parameters

def get_dict_from_json(url: str) -> dict:
    response = None
    try:
        response = urllib.request.urlopen(url)
        return json.loads(response.read().decode(encoding = 'utf-8'))
    finally:
        if response != None:
            response.close()
            
def get_results(json_text: 'json text') -> []:
    result_list = []
    
    for event in range(len(json_text['events']['event'])):
        if json_text['events']['event'][event]['image'] == None:
            result_list.append({'Title': json_text['events']['event'][event]['title'], 'Address': json_text['events']['event'][event]['venue_address'], 'EventURL': json_text['events']['event'][event]['url'], 'EventImageURL': None})
        else:
            result_list.append({'Title': json_text['events']['event'][event]['title'], 'Address': json_text['events']['event'][event]['venue_address'], 'EventURL': json_text['events']['event'][event]['url'], 'EventImageURL': json_text['events']['event'][event]['image']['thumb']['url']})
        
    return result_list  
         
         
# Test
print(build_url('Irvine, CA'))   
print(get_results(get_dict_from_json(build_url('Irvine, CA'))))