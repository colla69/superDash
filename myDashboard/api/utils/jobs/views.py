from django.shortcuts import render
from myDashboard.api.utils.jobs.jobData_handler import get_jobList
from myDashboard.forms import JobsRatingForm
from myDashboard.models import JobsRating


def get_ctx():
    js = get_jobList()

    rated = JobsRating.objects.values_list("job_id", flat=True)
    keyset = set(js.keys())
    for j in keyset:
        if j in rated:
            del js[j]
    ctx = {"jobs": js}
    return ctx


def jobs_view(request, *args, **kwargs):
    ctx = {"jobs": get_jobList()}
    return render(request, 'jobs_view.html', get_ctx())


def good_job(request, *args, **kwargs):
    form = JobsRatingForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'jobs_view.html', get_ctx())
