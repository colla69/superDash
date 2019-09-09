from apscheduler.schedulers.background import BackgroundScheduler
from myDashboard.api.utils.jobs.jobData_handler import cleanup_data_duplicates
from myDashboard.api.utils.save_sites import save_HTML_dump

scheduler = BackgroundScheduler()
job = None


def start_job():
    global job
    print("starting scheduled jobs.. ")
    # scheduler.add_job(check_online, 'interval', seconds=3600)
    scheduler.add_job(save_HTML_dump, 'interval', seconds=5000)
    scheduler.add_job(cleanup_data_duplicates, 'interval', seconds=10800)
    # save_HTML_dump()
    # cleanup_data_duplicates()
    try:
        scheduler.start()
    except:
        pass
