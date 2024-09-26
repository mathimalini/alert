from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def message(request):
    return render(request,"message.html")

def success(request):
    messages.success(request,"this is sucess message")
    return render(request,"message.html")




def info(request):
    messages.info(request,"this is info message")
    return render(request,"message.html")

def error(request):
    messages.error(request,"this is danger message")
    return render(request,"message.html")
    
    
def warning(request):
        messages.warning(request,"this is warning message")
        return render(request,"message.html")





