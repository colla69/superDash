
import requests
from bs4 import BeautifulSoup

def get_oneounchManga():
    url = ("https://www.mangareader.net")
    page = requests.get(url+"/onepunch-man")
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find_all("td")
    res = {}
    for link in links:
        try:
            if "Onepunch-Man" in link.text:
                a = link.find("a")
                res[ url+a["href"]] = link.text[2:]
                # print(link.text)
        except:
            continue
    return res


#print(get_oneounchManga())
