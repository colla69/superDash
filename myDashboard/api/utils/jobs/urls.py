from django.urls import path
from myDashboard.api.utils.jobs.views import jobs_view,good_job


urlpatterns = [
    path('jobSearch/', jobs_view, name="jobsView"),
    path('postGJ/', good_job, name="postGJ"),
]
