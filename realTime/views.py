#All the functions are added here

from django.http import HttpResponse
from django.http import JsonResponse
from django.template import Context, loader
from django.shortcuts import render
from .forms import realTimeModel
import json
import random
import re

userCheckFlag=0

def index(request):
    return HttpResponse("This is my First App")

def home(request):
    return render(request,'home.html')

def dataDisplay(request):
    p=realTimeModel.objects.get(id='12')
    degrees =p.humidity
    humidity =p.temperature
    hectopascals =p.pressure
    return render(request,'t.html',context={'degrees':degrees,'humidity':humidity,'hectopascals':hectopascals})

def returnSix(request):
    p1=realTimeModel.objects.get(id='12')
    p2=realTimeModel.objects.get(id='13')
    p3=realTimeModel.objects.get(id='14')
    p4=realTimeModel.objects.get(id='15')
    p5=realTimeModel.objects.get(id='16')
    p6=realTimeModel.objects.get(id='17')
    b1=p1.humidity
    b2=p2.temperature
    b3=p3.temperature
    b4=p4.temperature
    b5=p5.temperature
    b6=p6.temperature
    lat1=p1.temperature
    lat2=p2.humidity
    lat3=p3.humidity
    lat4=p4.humidity
    lat5=p5.humidity
    lat6=p6.humidity
    long1=p1.pressure
    long2=p2.pressure
    long3=p3.pressure
    long4=p4.pressure
    long5=p5.pressure
    long6=p6.pressure
    return JsonResponse({'item':[{'b':b1,'lat':lat1,'long':long1},{'b':b2,'lat':lat2,'long':long2},{'b':b3,'lat':lat3,'long':long3},{'b':b4,'lat':lat4,'long':long4},{'b':b5,'lat':lat5,'long':long5},{'b':b6,'lat':lat6,'long':long6}]})

def returnSixG(request):
    p1=realTimeModel.objects.get(id='12')
    p2=realTimeModel.objects.get(id='13')
    p3=realTimeModel.objects.get(id='14')
    p4=realTimeModel.objects.get(id='15')
    p5=realTimeModel.objects.get(id='16')
    p6=realTimeModel.objects.get(id='17')
    b1=p1.humidity
    b2=p2.temperature
    b3=p3.temperature
    b4=p4.temperature
    b5=p5.temperature
    b6=p6.temperature
    return JsonResponse({'b1':b1,'b2':b2,'b3':b3,'b4':b4,'b5':b5,'b6':b6})

def inData(request):
    attributeList=[f.name for f in realTimeModel._meta.get_fields()]
    upData=[]
    if request.method == "POST":
        for i in range(len(attributeList)):
        	upData.append((request.POST.get(attributeList[i])))
        forms=dict(zip(attributeList,upData))
    else:
        strRequest=str(request)
        for i in range(len(attributeList)):
                name=str(re.findall(attributeList[i]+":([a-zA-Z0-9]*),",strRequest))
           # name=str(re.findall(attributeList[i]+":([a-zA-Z0-9]*),",strRequest))
                name=name.rstrip("']")
                name=name.lstrip("['")
                upData.append(name)
                forms=dict(zip(attributeList,upData))
    #realTimeInstant=realTimeModel.objects.create(**for
    realTimeModel.objects.filter(id=forms['id']).update(**forms) 
    #realTimeInstant.save()
    #return JsonResponse(forms,safe=False
    #print(userCheckFlag)
    return HttpResponse(userCheckFlag)
def userStart(request):
    global userCheckFlag
    if request.method == "POST":
        userCheck=request.POST.get("userAnswer")
    else:
        strRequest=str(request)
        userCheck=(re.findall("userAnswer"+":([a-zA-Z0-9]*),",strRequest))
        userCheck=userCheck[0]
    print(userCheck)
    if userCheck=='1':
        userCheckFlag='1'
            #print("yes")
            #pop={'message':'success'}
            #return JsonResponse(pop,safe=False)
    elif userCheck=='0':
        userCheckFlag='0'
    elif userCheck=='3':
        userCheckFlag='3' 
    else:
        print('NO')
        pop={'message':'Success'}
    pop={'message':'success'}
    return render(request,'t.html')
        
def userResponse(request):
    global userCheckFlag
    try:
        if userCheckFlag=="1":
            userRes="1"
            #return JsonResponse(userRes, safe=False)
            #userCheckFlag=4
        elif userCheckFlag=="2":
            userRes="2"
            #userCheckFlag=4
        elif userCheckFlag=="0":
            userRes="0"
            #userCheckFlag="4"
        else:
            userRes="4"
        userCheckFlag='4'
        return HttpResponse(userRes)
    except:
        userRes={'userRes':4}
        userCheckFlag='0'
        return HttpResponse(userCheckFlag)

