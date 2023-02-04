from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from app.forms import *

# Create your views here.
def insert_topic(request):
    tfo=TopicForm()
    d={'topic':tfo}
    if request.method=='POST':
        fd=TopicForm(request.POST)
        if fd.is_valid():
            tn=fd.cleaned_data['topic_name']
            T=Topic.objects.get_or_create(topic_name=tn)[0]
            T.save()
            return HttpResponse('topic is inserted')

    return render(request,'insert_topic.html',d)

def topic_modelform(request):
    tmfo=ModelTopicForm()
    d={'modeltf':tmfo}
    if request.method=='POST':
        fd=ModelTopicForm(request.POST)
        if fd.is_valid():
            fd.save()
            return HttpResponse('topic is inserted by using model form')
    return render(request,'Topic_modelform.html',d)

def webpage_modelform(request):
    wmfo=ModelWebpageForm()
    d={'mwf':wmfo}
    if request.method=='POST':
        fd=ModelWebpageForm(request.POST)
        if fd.is_valid():
            fd.save()
            return HttpResponse('webpage is inserted by using model form')

    return render(request,'webpage_modelform.html',d)

def access_modelForm(request):
    amfo=ModelAccessForm()
    d={'amf':amfo}
    if request.method=='POST':
        fd=ModelAccessForm(request.POST)
        if fd.is_valid():
            fd.save()
            return HttpResponse('accessrecods is inserted by usung model form')
    return render(request,'access_modelform.html',d)    



    
    


















    return render(request,'insert_topic.html',d)
