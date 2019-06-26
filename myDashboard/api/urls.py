
from django.urls import path

from .views import uni_list

urlpatterns = [
    path('uniRest/', uni_list, name="uniList"),
]