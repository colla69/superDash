
import requests
from bs4 import BeautifulSoup

def get_bokunoheroacademiaManga():
    url = ("https://www.mangareader.net")
    page = requests.get(url+"/boku-no-hero-academia")
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find_all("td")
    res = {}
    for link in links:
        try:
            if "Boku no Hero Academia" in link.text:
                a = link.find("a")
                res[ url+a["href"]] = link.text[2:]
                # print(link.text)
        except:
            continue
    return res


print(get_bokunoheroacademiaManga())
