
import mechanicalsoup
from django.utils import timezone
from myDashboard.models import DataDump

links = [
    "https://www.careerjet.it/wcerca/lavoro?s=programmatore&l=Bologna&lid=41991&ct=p&nw=1",
    "https://www.kijiji.it/offerte-di-lavoro/offerta/annunci-bologna/informatica-e-web/",
]


def save_HTML_dump():
    browser = mechanicalsoup.StatefulBrowser()
    for link in links:
        browser.open(link)
        page = browser.get_current_page()
        DataDump.objects.create(
            time=timezone.now(),
            source=link,
            data=str(page)
    )
