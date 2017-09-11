from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from messageWallApp.models import MessageForm, Message
import re
import json
# Create your views here.
def messageSend(req):
    if req.method == 'POST':
        sendMessage = MessageForm(req.POST)
        if sendMessage.is_valid():
            if len(sendMessage.cleaned_data['messageText']) > 10:
                return HttpResponse('<h1>请勿超过10个字</h1>')
            message = Message()
            message.messageText = sendMessage.cleaned_data['messageText']
            message.isShow = False
            message.save()
            return HttpResponse('<h1>发送成功</h1>')
    else:
        message = MessageForm()
        return render(req, 'sendMessage.html', {'form': message})

def showMessage(req):
    messages = Message.objects.all()
    for message in messages:
        message.isShow = True
        message.save()
    return render(req, 'showMessage.html', {"messageList": messages})

def getMessage(req):
    messages = Message.objects.filter(isShow__exact = False)
    data = {"list": []}
    for message in messages:
        data["list"].append({"message": message.messageText})
        message.isShow = True
        message.save()
    
    jsonString = json.dumps(data)
    print(jsonString)
    response = HttpResponse(jsonString)
    response["Content-type"] = 'application/json'
    return response
