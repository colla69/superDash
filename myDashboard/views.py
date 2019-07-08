from django.http import HttpResponse
from django.shortcuts import render

import myDashboard.api.utils.manga.bokunoheroacademia_getter as bnha
import myDashboard.api.utils.manga.onepiece_getter as op
import myDashboard.api.utils.manga.onepunchman_getter as opm
from myDashboard.api.utils.jobs.jobData_handler import get_jobList
from myDashboard.api.utils.myIpTools.ip_track import save_ip, get_last_ip
from myDashboard.forms import DoneReading
from .models import DashApps, DoneLinksLog
# needed to start scheduler
from .schedule_events import start_job

start_job()


def home_view(request, *args, **kwargs):
    apps = DashApps.objects.all()
    ctx = {
        "apps": apps,
        "ip": get_last_ip()
    }
    return render(request, "appPanel.html", ctx)


def ip_view(request, *args, **kwargs):
    print("pingHome")
    try:
        # for k in request.META.keys():
        #     print(k + " " +request.META[k])
        client_address = request.META['HTTP_X_REAL_IP']
    except:
        client_address = ""
    if client_address:
        save_ip(client_address)
    return HttpResponse('OK')


def uni_view(request, *args, **kwargs):
    return render(request, "uniPanel.html")


def onepiece_view(request, *args, **kwargs):
    read_chap = get_read_chapters(op.get_onepieceManga())
    ctx = {
        "chapters": read_chap,
    }
    return render(request, "op_view.html", ctx)


def post_seen_op(request):
    form = DoneReading(request.POST or None)
    if form.is_valid():
        form.save()
    read_chap = get_read_chapters(op.get_onepieceManga())
    context = {
        'form': form,
        "chapters": read_chap,
    }
    return render(request, 'op_view.html', context)


def onepunchman_view(request, *args, **kwargs):
    read_chap = get_read_chapters(opm.get_oneounchManga())
    ctx = {
        "chapters": read_chap,
    }
    return render(request, "opm_view.html", ctx)


def post_seen_opm(request):
    form = DoneReading(request.POST or None)
    if form.is_valid():
        form.save()
    read_chap = get_read_chapters(opm.get_oneounchManga())
    context = {
        'form': form,
        "chapters": read_chap,
    }
    return render(request, 'opm_view.html', context)


def bnha_view(request, *args, **kwargs):
    read_chap = get_read_chapters(bnha.get_bokunoheroacademiaManga())
    ctx = {
        "chapters": read_chap,
    }
    return render(request, "bnha_view.html", ctx)


def post_seen_bnha(request):
    form = DoneReading(request.POST or None)
    if form.is_valid():
        form.save()
    read_chap = get_read_chapters(bnha.get_bokunoheroacademiaManga())
    context = {
        'form': form,
        "chapters": read_chap,
    }
    return render(request, 'bnha_view.html', context)


def get_read_chapters(chpts):
    chapters = []
    chapters = chpts
    read_chap = []
    gelesen = DoneLinksLog.objects.all()
    ids = set(done.link for done in gelesen)
    for key,val in chapters.items():
        if key in ids:
            read_chap.append((key, val, "Read"))
        else:
            read_chap.append((key, val, "Unread"))
    return read_chap


def jobs_view(request, *args, **kwargs):
    ctx = {"jobs": get_jobList()}
    return render(request, 'jobs_view.html', ctx)
