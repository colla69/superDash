
from django.http import JsonResponse

from myDashboard.api.utils.uni.uni_data import get_uni_data


def uni_list(request):
    data = get_uni_data()
    return JsonResponse(data)
