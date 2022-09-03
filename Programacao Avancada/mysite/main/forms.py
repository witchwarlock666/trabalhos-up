from django import forms

class addGame(forms.Form):
    appid = forms.CharField(max_length=15)
    
class searchGame(forms.Form):
    appid = forms.CharField(max_length=15)