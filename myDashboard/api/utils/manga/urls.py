
from django.urls import path

from myDashboard.api.utils.manga.views import onepiece_view, onepunchman_view, post_seen_opm, bnha_view, post_seen_bnha, \
    post_seen_op

urlpatterns = [
    path('op/', onepiece_view, name="op"),
    path('opPost/', post_seen_op, name="opPost"),
    path('opm/', onepunchman_view, name="opm"),
    path('opmPost/', post_seen_opm, name="opmPost"),
    path('bnha/', bnha_view, name="bnha"),
    path('bnhaPost/', post_seen_bnha, name="bnhaPost"),
]