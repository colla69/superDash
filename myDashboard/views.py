from django.shortcuts import render
from .models import DashApps, UniLink
import myDashboard.utils.algo_getter as algo

def home_view(request, *args, **kwargs):
    apps = DashApps.objects.all()
    ctx = {
        "apps": apps
    }
    return render(request, "appPanel.html", ctx)


def uni_view(request, *args, **kwargs):
    links = UniLink.objects.all()
    ub = algo.get_uebungen()
    cap = algo.get_vorlesungen()
    data = {}
    for link in links:
        if link.name == "ALGO":
            data[link.name] = [link, ub, cap]
        else:
            data[link.name] = [link, "", ""]
    ctx = {
        "VLs": data,
    }
    # print (data)
    return render(request, "uniPanel.html", ctx)
