'''
Created on Jan 20, 2017

@author: EltonXue
'''

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from django.views.generic import View
from .EventfulAPIModule import *
from .ImageSearchAPIModule import *

class Search(View):
    def get(self, request):
            
        now = datetime.datetime.now()
        
        
        
        return render(request, "main.html", Context({"now": now}))
    
    def post(self, request):
        location = request.POST.get('search')
        
        event_dict = get_dict_from_json(build_url(location))
        event_list = get_results(event_dict)
        
        now = datetime.datetime.now()
        
        
        
        self.event1 = event_list[0]
        self.event2 = event_list[1]
        self.event3 = event_list[2]
        self.event4 = event_list[3]
        self.event5 = event_list[4]
        self.event6 = event_list[5]
        self.event1["EventImageURL"] = parse_img(get_dict_from_json_img(create_json_img(self.event1["Title"])))
        self.event2["EventImageURL"] = parse_img(get_dict_from_json_img(create_json_img(self.event2["Title"])))
        self.event3["EventImageURL"] = parse_img(get_dict_from_json_img(create_json_img(self.event3["Title"])))
        self.event4["EventImageURL"] = parse_img(get_dict_from_json_img(create_json_img(self.event4["Title"])))
        self.event5["EventImageURL"] = parse_img(get_dict_from_json_img(create_json_img(self.event5["Title"])))
        self.event6["EventImageURL"] = parse_img(get_dict_from_json_img(create_json_img(self.event6["Title"])))
        
        return render(request, "activities.html", Context({"now": now, 
                                                     "event1": self.event1, 
                                                     "event2": self.event2, 
                                                     "event3": self.event3, 
                                                     "event4": self.event4, 
                                                     "event5": self.event5, 
                                                     "event6": self.event6}))
    
