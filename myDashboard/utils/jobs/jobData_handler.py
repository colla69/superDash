from bs4 import BeautifulSoup
from myDashboard.models import DataDump
from myDashboard.utils.jobs.kijiji_jobs import get_kiji
from myDashboard.utils.jobs.careerjet import get_careerjet_jobs


kijiji = "https://www.kijiji.it/offerte-di-lavoro/offerta/annunci-bologna/informatica-e-web/"
careerjet = "https://www.careerjet.it/wcerca/lavoro?s=programmatore&l=Bologna&lid=41991&ct=p&nw=1"

def get_jobList():
    res = {}
    jList = DataDump.objects.all().order_by('time')
    for job in jList:
        soup = BeautifulSoup(job.data, "html.parser")
        if kijiji == job.source:
            jobs = get_kiji(soup)
        elif careerjet == job.source:
            jobs = get_careerjet_jobs(soup)
        for j in jobs.keys():
            res[j] = jobs[j]
    return res

