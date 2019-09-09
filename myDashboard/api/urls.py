
from django.urls import path

from myDashboard.api.utils.uni.views import uni_list


urlpatterns = [
    path('uniRest/', uni_list, name="uniList"),
]