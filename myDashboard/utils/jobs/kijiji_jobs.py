
import mechanicalsoup
from os.path import expanduser, isfile


def get_kiji():
    print('getting Jobs from kijiji.. ')
    data_path = expanduser("/home/cola/jobs.json")
    res = {}
    link = "https://www.kijiji.it/offerte-di-lavoro/offerta/annunci-bologna/informatica-e-web/?entryPoint=sb"
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(link)
    searchres = browser.get_current_page().find("ul", id="search-result")

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
    print("done\n")


