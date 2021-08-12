# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("hello\n")
    
def index_v1(request):
    return HttpResponse("Hello, world. You're at the v1 index.\n")
    
def user_v1(request):
    return HttpResponse("Hello, world. You're at the v1 user api.\n")
    
def config_v1(request):
    return HttpResponse("Hello, world. You're at the v1 config api.\n")
    
def index_v2(request):
    return HttpResponse("Hello, world. You're at the v2 index.\n")
    
def user_v2(request):
    return HttpResponse("Hello, world. You're at the v2 user api.\n")
    
def config_v2(request):
    return HttpResponse("Hello, world. You're at the v2 config api.\n")