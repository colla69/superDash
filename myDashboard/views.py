from django.shortcuts import render
from .models import DashApps, UniLink
from .utils.html_utils import existinglink

def home_view(request, *args, **kwargs):
    apps = DashApps.objects.all()
    ctx = {
        "apps": apps
    }
    return render(request, "home_view.html", ctx)


def uni_view(request, *args, **kwargs):
    links = UniLink.objects.all()
    ctx = {
        "VLs": links,
    }
    return render(request, "uniPanel.html", ctx)


