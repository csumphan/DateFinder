# Parser.py

def get_results(json_text: 'json text') -> list:
    location_list = []
    
    for predictions in range(len(json_text['predictions'])):
        location_list.append(json_text['predictions'][predictions]['description'])
        
    return location_list
    