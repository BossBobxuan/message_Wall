from django.db import models
from django import forms
# Create your models here.
class MessageForm(forms.Form):
    messageText = forms.CharField(label = '内容',widget = forms.TextInput(attrs={'class':'weui_input','placeholder':'请勿超过10个字'}))
    

class Message(models.Model):
    messageText = models.CharField(max_length=100)
    isShow = models.BooleanField()
    