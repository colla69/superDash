import operator

from bs4 import BeautifulSoup

from myDashboard.api.utils.jobs.careerjet import get_careerjet_jobs
from myDashboard.api.utils.jobs.kijiji_jobs import get_kiji
from myDashboard.api.utils.jobs.linkedin import get_linkedin_jobs
from myDashboard.models import DataDump

kijiji = "https://www.kijiji.it/offerte-di-lavoro/offerta/annunci-bologna/informatica-e-web/"
careerjet = "https://www.careerjet.it/cerca/lavoro?s=programmatore&l=Bologna&lid=41991&ct=p&nw=1"
linkedin = "https://it.linkedin.com/"


def get_jobList():
    res = {}
    datalist = {}
    count = DataDump.objects.all().count()  # 1 million
    chunk_size = 500
    joblist = DataDump.objects.defer("data").order_by("-time")
    # joblist = joblist[:50]
    """for i in range(0, count, chunk_size):
        joblist = DataDump.objects.defer("data").order_by("-time")[i:i+chunk_size]"""
    for job in joblist[:100]:
        if job.source not in datalist.keys():
            html_data = job.data
            if "python" in html_data:
                data = BeautifulSoup(html_data, "html.parser")
                datalist[job.source] = job.time, data
    for key, job in datalist.items():
        time = job[0]
        soup = job[1]
        if kijiji == key:
            jobs = get_kiji(soup, time)
        elif careerjet == key:
            jobs = get_careerjet_jobs(soup, time)
        elif linkedin in key:
            jobs = get_linkedin_jobs(soup, time, key)
        try:
            for j in jobs.keys():
                res[j] = jobs[j]
        except UnboundLocalError:
            continue
    return res


def cleanup_data_duplicates():
    print("starting cleanup .. ", end="")
    res = {}
    datalist = {}
    datalist = DataDump.objects.all()
    ordered = sorted(datalist, key=operator.attrgetter('time'), reverse=True)
    known = []
    count = 0
    for o in ordered:
        if o.source in known:
            o.delete()
            count += 1
            continue
        else:
            known.append(o.source)
    print("done!  deleted: "+str(count)+" lines")
