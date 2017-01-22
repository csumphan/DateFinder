
########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, json

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'c610f93b616647a393ecce4076c27db1',
}
def create_json_img(searchkey):
    params = urllib.parse.urlencode({
        # Request parameters
        'q': searchkey,
        'count': '1',
        'offset': '0',
        'mkt': 'en-us',
        'safeSearch': 'Moderate',
        'size': 'large',
    })

    try:
        conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
        conn.request("GET", "/bing/v5.0/images/search?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data.decode("utf-8")
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
        

def get_dict_from_json_img(str_json) -> dict:
    response = None
    try:
        return json.loads(str_json)
    finally:
        if response != None:
            response.close()
             
def parse_img(json_text: 'json text'):   
    return json_text['value'][0]['contentUrl']




