from datetime import datetime,timezone
from myDashboard.models import IpLog

lastupdate = datetime.now()

def save_ip(new_ip):
    last_ip = get_last_ip()
    if new_ip:
        if last_ip != new_ip:
            now = datetime.now(timezone.utc)
            new_ip = IpLog.objects.create(ip=new_ip, time=now)

def get_last_ip():
    return IpLog.objects.last().ip

