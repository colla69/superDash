from datetime import datetime
from myDashboard.models import IpLog

def save_ip(new_ip):
    last_ip = last_ip()
    if new_ip:
        if last_ip != new_ip:
            new_ip = IpLog.objects.create(ip=new_ip, time=datetime.now())

def last_ip():
    return IpLog.objects.last().ip

