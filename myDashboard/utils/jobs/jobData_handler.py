from bs4 import BeautifulSoup
from myDashboard.models import DataDump
from myDashboard.utils.jobs.kijiji_jobs import get_kiji
from myDashboard.utils.jobs.careerjet import get_careerjet_jobs


kijiji = "https://www.kijiji.it/offerte-di-lavoro/offerta/annunci-bologna/informatica-e-web/"
careerjet = "https://www.careerjet.it"

def get_jobList():
    res = {}
    jList = DataDump.objects.all()
    for job in jList:
        soup = BeautifulSoup(job.data, "html.parser")
        jobs = []
        if kijiji in job.source:
            jobs = get_kiji(soup)
        elif careerjet in job.source:
            jobs = get_careerjet_jobs(soup)
        for j in jobs.keys():
            res[j] = jobs[j]
    return res

