import os
import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.db.models import Count, Avg
from array import *
from .models import *
from django.db.models import F
from datetime import timedelta
from django.utils import timezone
from django.core import serializers

@login_required(login_url='/accounts/login/')
def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))
def poxlogs(request):
    return render_to_response('poxlogs.html', context_instance=RequestContext(request))
def tempflows(request):
    timeisnow=datetime.datetime.now() - timedelta(minutes=1)
    tempf = TemporaryFlows.objects.values ('switchport','ip_src','ip_dst', 'dst_port').filter(timestamp__gte=timeisnow).annotate(num_ports=Count('dst_port'))
   # tempf2 = TemporaryFlows.objects.values ('ip_src', 'dst_port').annotate(num_ports=Count('dst_port')) 
   #tempf = Switchs.objects.filter('name_switch', temporary_flows_id_temporaryflow='fl')
    return render_to_response('tempflows.html',
    RequestContext(request, {'tempf':tempf}))
def installedflows(request):
   # flows = TemporaryFlows.objects.all()
   # for flow in flows:
    #  flow.flows = Switchs.objects.filter(temporary_flows_id_temporaryflow__id = flows.id_switch)
   # return render(request, "installedflows.html", {'flows': flows})
    flows = TemporaryFlows.objects.all().order_by('id_temporaryflow').reverse()
    return render_to_response('installedflows.html',
    RequestContext(request, {'flows':flows}))
def poxstatus(request):
    status = UsageTable.objects.filter(servername = 'POX')
    time5=datetime.datetime.now() - timedelta(minutes=5)
    time4=datetime.datetime.now() - timedelta(minutes=4)
    time3=datetime.datetime.now() - timedelta(minutes=3)
    time2=datetime.datetime.now() - timedelta(minutes=2)
    time1=datetime.datetime.now() - timedelta(minutes=1)
    req1 =  TemporaryFlows.objects.filter(timestamp__gte=time1).count()
    req2 =  TemporaryFlows.objects.filter(timestamp__gte=time2).count() - req1
    req3 =  TemporaryFlows.objects.filter(timestamp__gte=time3).count() - req2
    req4 =  TemporaryFlows.objects.filter(timestamp__gte=time4).count() - req3
    req5 =  TemporaryFlows.objects.filter(timestamp__gte=time5).count() - req4
    return render_to_response('poxstatus.html',
    RequestContext(request, {'status':status, 'req1':req1,'req2':req2,'req3':req3,'req4':req4,'req5':req5}))
def honeypotstatus(request):
    return render_to_response('honeypotstatus.html', context_instance=RequestContext(request))
def about(request):
    return render_to_response('about.html', context_instance=RequestContext(request))
def rules(request):
    rules = RuleTable.objects.all().order_by('id_rule').reverse()
    for rule in rules:
      if (rule.action == 'mod_nw_dst:10.0.0.2'):
	rule.action = 'DST ao HoneyPot'
      else:
	rule.action = 'DROP'
    return render_to_response('rules.html',
    RequestContext(request, {'rules':rules}))

