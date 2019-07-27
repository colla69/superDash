import mechanicalsoup
from django.utils import timezone

from myDashboard.models import DataDump
from .jobs.careerjet import get_careerjet_single_links
from .jobs.linkedin import save_linkedin

careerjet = "https://www.careerjet.it/cerca/lavoro?s=programmatore&l=Bologna&lid=41991&ct=p&nw=1"
links = [
    "https://www.kijiji.it/offerte-di-lavoro/offerta/annunci-bologna/informatica-e-web/",
    careerjet,
]


def add_carrer_jet():
    c_links = get_careerjet_single_links("https://www.careerjet.it/cerca/lavoro?s=programmatore&l=Bologna&lid=41991&ct=p&nw=1")
    for l in c_links:
        links.append(l)


def save_HTML_dump():
    print("saving websites ... ", end="")
    save_linkedin()
    add_carrer_jet()
    browser = mechanicalsoup.StatefulBrowser()
    for link in links:
        browser.open(link)
        page = browser.get_current_page()
        DataDump.objects.create(
            time=timezone.now(),
            source=link,
            data=str(page)
        )
    print("done!")
