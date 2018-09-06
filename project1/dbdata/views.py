from django.shortcuts import render
from datetime import datetime
# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse(content="Hi You are at the index of dbdata app")
    # print ("Request: ",request)
    # return HttpResponse(content=request)

def otherindex(request):
    # return HttpResponse(content="Hi You are at the other index")
    # print ("Request: ",request)
    return HttpResponse(content=str(datetime.now()))

def details(request, name):
    return HttpResponse("You requested for name %s." % name)

def results(request, name):
    response = "Results for name %s."
    return HttpResponse(response % name)