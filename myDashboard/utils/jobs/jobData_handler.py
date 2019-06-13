from bs4 import BeautifulSoup
from myDashboard.models import DataDump
from myDashboard.utils.jobs.kijiji_jobs import get_kiji
from myDashboard.utils.jobs.careerjet import get_careerjet_jobs
from django.utils import timezone


kijiji = "https://www.kijiji.it/offerte-di-lavoro/offerta/annunci-bologna/informatica-e-web/"
careerjet = "https://www.careerjet.it/wcerca/lavoro?s=programmatore&l=Bologna&lid=41991&ct=p&nw=1"


def get_jobList():
    res = {}
    datalist = {}
    count = DataDump.objects.all().count()  # 1 million
    chunk_size = 500
    for i in range(0, count, chunk_size):
        joblist = DataDump.objects.defer("data").order_by("-time")[i:i+chunk_size]
        for job in joblist:
            if not job.source in datalist.keys():
                data = BeautifulSoup(job.data, "html.parser")
                datalist[job.source] = job.time, data
    for key, job in datalist.items():
        time = job[0]
        soup = job[1]
        if kijiji == key:
            jobs = get_kiji(soup, time)
        elif careerjet == key:
            jobs = get_careerjet_jobs(soup, time)
        try:
            for j in jobs.keys():
                res[j] = jobs[j]
        except UnboundLocalError:
            continue
    return res

