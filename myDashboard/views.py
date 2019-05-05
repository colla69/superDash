from django.shortcuts import render
from .models import DashApps, UniLink


def home_view(request, *args, **kwargs):
    apps = DashApps.objects.all()
    ctx = {
        "apps": apps
    }
    return render(request, "appPanel.html", ctx)


def uni_view(request, *args, **kwargs):
    links = UniLink.objects.all()
    ctx = {
        "VLs": links
    }
    return render(request, "uniPanel.html", ctx)


