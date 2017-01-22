from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=32,widget=forms.PasswordInput)
    class Meta:
        #info about the class
        
        model = User
        
        fields = ['username','email','password']
        
            
        