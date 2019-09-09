
from django.urls import path

from myDashboard.api.utils.myIpTools.views import visitors_view, ip_view

urlpatterns = [
    path('ip/', ip_view, name="ip"),
    path('cvvisitors/', visitors_view, name="cvvisitors"),
]