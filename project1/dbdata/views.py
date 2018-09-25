from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
# Create your views here.

from django.http import HttpResponse
from .models import Table1, Table2
from .forms import Form

def index(request):
    return HttpResponse(content="Hi You are at the index of dbdata app")
    # print ("Request: ",request)
    # return HttpResponse(content=request)

def otherindex(request):
    # return HttpResponse(content="Hi You are at the other index")
    # print ("Request: ",request)
    return HttpResponse(content=str(datetime.now()))

def details(request, name):
    user_data= Table1.objects.get(fname=name)
    return render(request, 'dbdata/details.html', {'name':name, 'user_data':user_data})
    # return HttpResponse("You requested for name %s." % name)

def results(request):
    all_data= Table1.objects.all()
    return render(request, 'dbdata/results.html', {'all_data':list(all_data)})
    # response = "Results for name %s."
    # return HttpResponse(response % name)

def result_detailed(request, data):
    name=data
    user_data= get_object_or_404(Table1, fname=name)
    return render(request, 'dbdata/result_detail.html', {'name':name, 'user_data':user_data})
    # response = "Results for name %s."
    # return HttpResponse(response % name)


def details_new(request):
    print ("Request Method is: ",request.method)
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=True)
            return redirect('detailed',data=new_entry.fname)
    else:
            # print ("Form Details Submitted: ",form)
        form = Form()
    return render(request, 'dbdata/details_new.html', {'form':form})
    # response = "Results for name %s."
    # return HttpResponse(response % name)
    