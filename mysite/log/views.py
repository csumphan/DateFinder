from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

from django.views.generic import View
from .forms import UserForm

class UserFormView(View):
    form_class = UserForm
    template_name = 'registration.html'
    
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name, {'form': form})
    
    #process and add them to database
    def post(self,request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            
            #does not save to database yet
            user = form.save(commit=False)
    
            #cleaned (normalized) data - data that is formatted properly 
            #make it ready to enter database
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            #hashes the password
            user.set_password(password)
            
            user.save()
            
            user = authenticate(username=username, password = password)
            
            if user is not None:
                
                if user.is_active:
                    
                    login(request,user)
                    
                    return redirect('main/')
                
        return render(request, self.template_name, {'form': form})
            
            
            
            
            
