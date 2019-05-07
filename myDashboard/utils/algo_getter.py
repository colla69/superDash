from lxml import html
import requests
from bs4 import BeautifulSoup


# uebungen
def get_uebungen():
    page = requests.get('http://www.dbs.ifi.lmu.de/cms/studium_lehre/lehre_bachelor/algodat19/index.html')
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find_all("td")
    res = {}
    lastname = ""
    for link in links:

        for a in link.find_all("a"):
            try:
                if a.text == "":
                    continue
                elif a.text == "Lsg":
                    res[lastname+"_"+a.text] = a["href"]
                else:
                    res[a.text] = a["href"]
                lastname = a.text
            except:
                res[a.text] = ""
            print(a.text+" "+a["href"])
    return res


# vorlesungen
def get_vorlesungen():
    page = requests.get('http://www.dbs.ifi.lmu.de/cms/studium_lehre/lehre_bachelor/algodat19/index.html')
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find_all("p")
    res = {}
    for link in links:
        if "Kapitel" in link.text:
            try:
                for a in link.find_all("a"):
                    res[link.text] = a["href"]
            except:
                res[link.text] = ""
            # print(link)
    return res
