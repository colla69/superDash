from django.shortcuts import render
from .models import DashApps, UniLink
import myDashboard.utils.algo_getter as algo
import myDashboard.utils.rnvs_getter as rnvs

def home_view(request, *args, **kwargs):
    apps = DashApps.objects.all()
    ctx = {
        "apps": apps
    }
    return render(request, "appPanel.html", ctx)


def uni_view(request, *args, **kwargs):
    links = UniLink.objects.all()
    data = {}
    for link in links:
        if link.name == "ALGO":
            data[link.name] = [link, algo.get_uebungen(), algo.get_vorlesungen()]
        elif link.name == "RNVS":
            data[link.name] = [link,  rnvs.get_uebungen(), rnvs.get_vorlesungen()]
        else:
            data[link.name] = [link, "", ""]
    ctx = {
        "VLs": data,
    }
    # print (data)
    return render(request, "uniPanel.html", ctx)
