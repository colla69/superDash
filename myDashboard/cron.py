
from myDashboard.utils.kijiji_jobs import get_kiji
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
job = None

@kronos.register('* * * * *')
def complain():
    res = get_kiji()
    print(get_kiji())

