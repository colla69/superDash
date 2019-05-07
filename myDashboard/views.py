from django.shortcuts import render
from .models import DashApps, UniLink, DoneLinksLog
import myDashboard.utils.algo_getter as algo
import myDashboard.utils.rnvs_getter as rnvs
import myDashboard.utils.onepiece_getter as op
from myDashboard.forms import DoneReading


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


def onepiece_view(request, *args, **kwargs):
    read_chap = get_read_chapters()
    ctx = {
        "chapters": read_chap,
    }
    return render(request, "mangaPanel.html", ctx)


def post_seen_op(request):
    form = DoneReading(request.POST or None)
    if form.is_valid():
        form.save()
    read_chap = get_read_chapters()
    context = {
        'form': form,
        "chapters": read_chap,
    }
    return render(request, 'mangaPanel.html', context)


def get_read_chapters():
    chapters = []
    chapters = op.get_onepieceManga()
    read_chap = []
    gelesen = DoneLinksLog.objects.all()
    ids = set(done.link for done in gelesen)
    for key,val in chapters.items():
        if key in ids:
            read_chap.append((key, val, "Read"))
        else:
            read_chap.append((key, val, "Unread"))
    return read_chap