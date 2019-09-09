from django.shortcuts import render
from myDashboard.api.utils.jobs.jobData_handler import get_jobList


def jobs_view(request, *args, **kwargs):
    ctx = {"jobs": get_jobList()}
    return render(request, 'jobs_view.html', ctx)


def post_goodjob(request):
    form = JobsRatingForm(request.POST or None)
    if form.is_valid():
        form.save()
    read_chap = get_read_chapters(opm.get_oneounchManga())
    context = {
        'form': form,
        "chapters": read_chap,
    }
    return render(request, 'opm_view.html', context)


def post_goodjob(request):
    form = JobsRatingForm(request.POST or None)
    if form.is_valid():
        form.save()
    read_chap = get_read_chapters(opm.get_oneounchManga())
    context = {
        'form': form,
        "chapters": read_chap,
    }
    return render(request, 'opm_view.html', context)
