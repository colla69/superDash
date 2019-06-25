from apscheduler.schedulers.background import BackgroundScheduler
from .myIpTools.site_checker import check_online
from .save_sites import save_HTML_dump

scheduler = BackgroundScheduler()
job = None


def start_job():
    global job
    print("starting scheduled jobs.. ")
    scheduler.add_job(check_online, 'interval', seconds=3600)
    scheduler.add_job(save_HTML_dump, 'interval', seconds=86400)
    # save_HTML_dump()
    try:
        scheduler.start()
    except:
        pass
    print("done!\n")

start_job()