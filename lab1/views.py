from django.shortcuts import render
from django.http import HttpResponse
import datetime

def current_time(request):
    return HttpResponse("The time is "+str(datetime.datetime.now()))



