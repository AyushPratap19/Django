from django.shortcuts import render
from django.http import HttpResponse
import datetime

def increase(request,offset):
   return HttpResponse("After "+str(offset)+" hours the time will be "+str(datetime.datetime.now()+datetime.timedelta(hours = offset)))

def decrease(request,offset):
    return HttpResponse("Before "+str(offset)+" hours time was "+str(datetime.datetime.now()-datetime.timedelta(hours=offset)))