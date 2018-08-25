from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    # here we can process the request data
    return HttpResponse('Hi this is hello index page screen')