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


class Search(View):
    
    def get(self, request):
            
        now = datetime.datetime.now()
    
        event1 = {"title": "Apple Picking", "address": "113 Cornell, Irvine, CA"}
        event2 = {"title": "Shopping", "address": "Tanforan Mall, San Bruno, CA"}
        
        context = Context({"now": now, "event1": event1, "event2": event2})
        
        return render(request, "main.html", context)
    
    def post(self, request):
        location = request.POST.get('search')
        
        
        return render(request, "main.html", Context({"now": location}))     
        
        


