# -*- coding: utf-8 -*-


import requests
from django.http import HttpResponse

from myDashboard.api.utils.manga.views import *
from myDashboard.api.utils.myIpTools.ip_track import save_ip
from myDashboard.api.utils.myIpTools.viewDNS_endpoints import *
from myDashboard.models import IpLog
# needed to start scheduler
from myDashboard.schedule_events import start_job

start_job()


def ip_view(request, *args, **kwargs):
    print("pingHome")
    try:
        client_address = request.META['HTTP_X_REAL_IP']
    except:
        client_address = ""
    if client_address:
        save_ip(client_address)
    return HttpResponse('OK')


def visitors_view(request, *args, **kwargs):
    myIpsQS = IpLog.objects.all().values_list("ip", flat=True)
    myIps = [i for i in myIpsQS]
    myIps.append("127.0.0.1")
    myIps.append("66.249.79.248")
    myIps.append("172.27.0.1")
    myIps.append("66.249.70.5")
    myIps.append("0:0:0:0:0:0:0:1")

    response = requests.get("https://cv.colarietitosti.info/visitors")
    ips = response.json()
    ctx = { "ips": []}
    for k in reversed(ips):
        ipaddr = k["ip_addr"]
        if ipaddr in myIps or ipaddr == "":
            continue
        else:
            timestamp = k["timestamp"]
            ctx["ips"].append((
                ipaddr,
                k["locale"],
                k["referer"],
                timestamp,
                get_ip_location(ipaddr),
                get_ip_whois(ipaddr),
                get_reverse_dns(ipaddr),
                get_port_scan(ipaddr)
            ))
    return render(request, 'cvVisitorsView.html', ctx)
