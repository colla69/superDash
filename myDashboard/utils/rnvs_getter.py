from lxml import html
import requests
from bs4 import BeautifulSoup
from superDash.psw import uni_psw

homepage = "http://www.nm.ifi.lmu.de/teaching/Vorlesungen/2019ss/rn/"
home = "https://uniworx.ifi.lmu.de/"

# uebungen
def get_uebungen():
    payload = {'username': "a.colarieti", 'password': uni_psw()}
    session = requests.Session()
    r = session.get("https://uniworx.ifi.lmu.de/?action=uniworxLogin")
    cookies = dict(r.cookies)
    login = session.post("https://uniworx.ifi.lmu.de/?action=uniworxLoginDo", data=payload,cookies=cookies)
    page = session.get("https://uniworx.ifi.lmu.de/?action=uniworxSheetListUser&id=1089", cookies=cookies)
    # print(page.text)
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find_all("tr")
    res = {}
    ix = 0
    for l in links:
        try:
            l["style"]
        except:
            for a in l.find_all("a"):
                if a.text == "" and \
                        not ("Correction" in a["href"]) and\
                        (a["href"] != "#"):
                    ix += 1
                    res["Übung"+str(ix)] = home+a["href"]

    return sorted(res, reverse=False)



# vorlesungen
def get_vorlesungen():
    home = "http://www.nm.ifi.lmu.de/teaching/Vorlesungen/2019ss/rn/"
    page = requests.post(home, verify=False)
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find_all("ol")
    res = {}
    for link in links:
        if "Kapitel" in link.text:
            try:
                for li in link.find_all("li"):
                    for a in li.find_all("a"):
                        res[li.text.strip("[pptx] [pdf]")] = home+a["href"]
            except:
                res[link.text] = ""
            # print(link)
    return res


