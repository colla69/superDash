from django.shortcuts import render
from myDashboard.api.utils.jobs.jobData_handler import get_jobList


def jobs_view(request, *args, **kwargs):
    ctx = {"jobs": get_jobList()}
    return render(request, 'jobs_view.html', ctx)
