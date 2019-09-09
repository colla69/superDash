# -*- coding: utf-8 -*-

from django.shortcuts import render

from myDashboard.api.utils.myIpTools.ip_track import get_last_ip
from .models import DashApps
from .schedule_events import start_job

start_job()


def home_view(request, *args, **kwargs):
    apps = DashApps.objects.all()
    ctx = {
        "apps": apps,
        "ip": get_last_ip()
    }
    return render(request, "appPanel.html", ctx)


def uni_view(request, *args, **kwargs):
    return render(request, "uniPanel.html")


def jobs_view(request, *args, **kwargs):
    ctx = {"jobs": get_jobList()}
    return render(request, 'jobs_view.html', ctx)

