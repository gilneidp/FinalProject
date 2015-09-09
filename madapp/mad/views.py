import os
import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from array import *
from .models import *
from django.db.models import F
from datetime import timedelta
from django.utils import timezone
from django.core import serializers

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))
def poxlogs(request):
    return render_to_response('poxlogs.html', context_instance=RequestContext(request))
def tempflows(request):
    return render_to_response('tempflows.html', context_instance=RequestContext(request))
def poxstatus(request):
    return render_to_response('poxsatus.html', context_instance=RequestContext(request))
def honeypotstatus(request):
    return render_to_response('honeypotstatus.html', context_instance=RequestContext(request))
def about(request):
    return render_to_response('about.html', context_instance=RequestContext(request))

