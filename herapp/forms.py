from typing import Text
from django import forms
from django.forms import widgets
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']
        widgets= {
            'name' : forms.TextInput(attrs={'placeholder':"İsminizi Giriniz",'class':'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder':"Emailinizi Giriniz",'class':'form-control'}),
            'message': forms.Textarea(attrs={'placeholder':"Mesajınızı Giriniz", 'class':'form-control'})
        }