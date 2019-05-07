
import requests
from bs4 import BeautifulSoup

def get_onepieceManga():
    url = ("https://www.mangareader.net")
    page = requests.get(url+"/one-piece")
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find_all("td")
    res = {}
    for link in links:
        try:
            if "One Piece" in link.text:
                a = link.find("a")
                res[link.text[2:]] = url+a["href"]
                #print(link.text)
        except:
            continue
    return res


#print(get_onepieceManga())