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

class Search(View):
    def get(self, request):
            
        now = datetime.datetime.now()
        
        
        
        return render(request, "main.html")
    
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
        
        return render(request, "activities.html", Context({"now": now, 
                                                     "event1": self.event1, 
                                                     "event2": self.event2, 
                                                     "event3": self.event3, 
                                                     "event4": self.event4, 
                                                     "event5": self.event5, 
                                                     "event6": self.event6}))
    
