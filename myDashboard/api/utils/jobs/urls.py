from django.urls import path
from myDashboard.api.utils.jobs.views import jobs_view


urlpatterns = [
    path('jobSearch/', jobs_view, name="jobsView"),
    # path('goodJob/', post_seen_op, name="opPost"),
]