from datetime import datetime

from myDashboard.models import IpLog


def save_ip(new_ip):
    last_ip = get_last_ip()
    now = datetime.now()
    if new_ip:
        if last_ip != new_ip:
            new_ip = IpLog.objects.create(ip=new_ip, time=now)


def get_last_ip():
    return IpLog.objects.last().ip

