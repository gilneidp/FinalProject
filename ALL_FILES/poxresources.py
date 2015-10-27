import os
import sys
import datetime
from datetime import timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "madapp.settings")
from django.core.management import execute_from_command_line
from django.db.models import Count, Avg

from madapp import settings
from madapp.mad.models import *

import psutil
cpu = psutil.cpu_times()
memory_used = psutil.virtual_memory()
memory_free = (memory_used.free/1024)/1024
#oxstats = UsageTable.objects.get(servername = 'POX')
#oxstats.cpu_usage = cpu
#oxstats.save()
print cpu
#print (((memory_used.used/1024)/1024)*100)/(((memory_used.free/1024)/1024) + ((memory_used.used/1024)/1024))
#print (memory_used.used/1024)/1024
#print ((memory_used.free/1024)/1024) + ((memory_used.used/1024)/1024)
#print cpu
#print memory_used.percent
