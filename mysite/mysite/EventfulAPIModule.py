import urllib.request         # urllib.request.urlopen(url)
import urllib.parse           # urllib.parse.urlencode((parameter, value))
import json

KEY = 'WcHjThBZW5Kmd66V'
BASE_URL = 'http://api.eventful.com/json/events/search?'
MONTHS = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'Jun.', 'Jul.', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']

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
            
def get_results(json_text: 'json text') -> list:
    result_list = []
    address_list = []
    
    for event in range(len(json_text['events']['event'])):
        if json_text['events']['event'][event]['venue_address'] in address_list:
            pass
        else:
            if json_text['events']['event'][event]['image'] == None:
                result_list.append({'Title': json_text['events']['event'][event]['title'], 'Address': json_text['events']['event'][event]['venue_address'], 'EventURL': json_text['events']['event'][event]['url'], 'Date': json_text['events']['event'][event]['start_time'], 'EventImageURL': None})
                address_list.append(json_text['events']['event'][event]['venue_address'])
            else:
                result_list.append({'Title': json_text['events']['event'][event]['title'], 'Address': json_text['events']['event'][event]['venue_address'], 'EventURL': json_text['events']['event'][event]['url'], 'Date': json_text['events']['event'][event]['start_time'], 'EventImageURL': json_text['events']['event'][event]['image']['medium']['url']})
                address_list.append(json_text['events']['event'][event]['venue_address'])
    
    for result in range(len(result_list)):
        if len(result_list[result]['Title']) >= 26:
            new_title = ''
            for letter in range(26):
                new_title += result_list[result]['Title'][letter]
            new_title += '...'
            result_list[result]['Title'] = new_title
            
        new_date = ''
        date_time = result_list[result]['Date'].split()
        date = date_time[0].split('-')
        time = date_time[1].split(':')
        new_date += MONTHS[int(date[1])-1] + " " + date[2] + ', ' + date[0] + ' @ '
        if int(time[0]) == 0:
            new_date += str(12) + ':' + time[1]
        else:    
            new_date += str(int(time[0])%12) + ':' + time[1]
        if int(time[0])//12 >= 1:
            new_date += 'pm'
        else:
            new_date += 'am'
        result_list[result]['Date'] = new_date
        
    return result_list  
         
         
# Test
# print(build_url('Los Angeles, CA'))   
# print(get_results(get_dict_from_json(build_url('Los Angeles, CA'))))