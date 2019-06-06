import myDashboard.utils.uni.promo_getter as promo
import myDashboard.utils.uni.algo_getter as algo
import myDashboard.utils.uni.rnvs_getter as rnvs
from myDashboard.models import UniLink
import threading
# from myDashboard.utils.kijiji_jobs import start_job


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
            data[link.name] = [link, result_data["promo_ub"], result_data["promo_v"]]
        elif link.name == "ALGO":
            data[link.name] = [link, result_data["algo_ub"], result_data["algo_v"]]
        elif link.name == "RNVS":
            data[link.name] = [link, result_data["rnvs_ub"], result_data["rnvs_v"]]
        else:
            data[link.name] = [link, "", ""]

    return data


#get_uni_data()
