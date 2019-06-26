import threading

import myDashboard.api.utils.uni.algo_getter as algo
import myDashboard.api.utils.uni.promo_getter as promo
import myDashboard.api.utils.uni.rnvs_getter as rnvs
from myDashboard.models import UniLink

# start_job()
result_data = {}


def get_algo_ub():
    result_data["algo_ub"] = algo.get_uebungen()


def get_algo_v():
    result_data["algo_v"] = algo.get_vorlesungen()


def get_promo_ub():
    result_data["promo_ub"] = promo.get_uebungen()


def get_promo_v():
    result_data["promo_v"] = promo.get_vorlesungen()


def get_rnvs_ub():
    result_data["rnvs_ub"] = rnvs.get_uebungen()


def get_rnvs_v():
    result_data["rnvs_v"] = rnvs.get_vorlesungen()


def get_uni_data():
    links = UniLink.objects.all()

    j_link = [entry for entry in UniLink.objects.values()]

    threads = [threading.Thread(target=get_rnvs_ub),
               threading.Thread(target=get_rnvs_v),
               threading.Thread(target=get_promo_ub),
               threading.Thread(target=get_promo_v),
               threading.Thread(target=get_algo_ub),
               threading.Thread(target=get_algo_v),
              ]

    for x in threads:
        x.start()
    # Wait for all of them to finish
    for x in threads:
        x.join()

    data = {}
    for link in links:
        if link.name == "Promo":
            data[link.name] = [j_link, result_data["promo_ub"], result_data["promo_v"]]
        elif link.name == "ALGO":
            data[link.name] = [j_link, result_data["algo_ub"], result_data["algo_v"]]
        elif link.name == "RNVS":
            data[link.name] = [j_link, result_data["rnvs_ub"], result_data["rnvs_v"]]
        else:
            data[link.name] = [j_link, "", ""]
    return data


#get_uni_data()
