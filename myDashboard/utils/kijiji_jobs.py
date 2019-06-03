
import mechanicalsoup
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from myDashboard.utils.json_ops import json_load,json_save
from os.path import expanduser

# scheduler = BlockingScheduler()
scheduler = BackgroundScheduler()
job = None


def start_job():
    global job
    #job = scheduler.add_job(get_kiji, 'interval', seconds=3600)
    job = scheduler.add_job(get_kiji, 'interval', seconds=200)
    get_kiji()
    try:
        scheduler.start()
    except:
        pass


def get_kiji():
    print('getting Jobs from kijiji.. ')
    data_path = expanduser("/home/cola/jobs.json")
    link = "https://www.kijiji.it/offerte-di-lavoro/offerta/annunci-bologna/informatica-e-web/?entryPoint=sb"
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(link)
    searchres = browser.get_current_page().find("ul", id="search-result")
    res = json_load(data_path)
    for li in searchres.find_all("li"):
        loc = li.find("p", class_="locale")
        if loc is None:
            continue
        if loc.text.lower() == "bologna":
            title = li.find("a", class_="cta").text.strip()
            link = li.find("a", class_="cta")["href"]
            description = li.find("p", class_="description").text

            res[link] = {"title": title,
                         "link": link,
                         "description": description
                         }
    print(res)
    json_save(res, data_path)
    print("done\n")

#print(res)
