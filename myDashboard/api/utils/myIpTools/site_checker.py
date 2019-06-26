import os

import mechanicalsoup
from django.utils import timezone

from myDashboard import CheckSitesLog

checklist = [
    "https://cv.colarietitosti.info",
    "https://plex.colarietitosti.info",
    "https://nextcloud.colarietitosti.info",
    "https://collabora.colarietitosti.info",
    "https://admin.colarietitosti.info",
]


def check_collabora():
    check = os.system('curl -k "http://collabora.colarietitosti.info:9980"')
    if 13312 == check:
        return True
    else:
        return False


def check_online():
    CheckSitesLog.objects.all().delete()
    browser = mechanicalsoup.StatefulBrowser()
    for link in checklist:
        if link == "https://collabora.colarietitosti.info":
            status = check_collabora()
            continue
        response = browser.open(link)
        if response.status_code != 502:
            status = True
        else:
            status = False
        entry = CheckSitesLog.objects.create(site=link, time=timezone.now(), status=status)
        entry.save()
    # print(res)
