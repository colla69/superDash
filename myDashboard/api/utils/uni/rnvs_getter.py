import requests
from bs4 import BeautifulSoup

from superDash.psw import uni_psw

homepage = "http://www.nm.ifi.lmu.de/teaching/Vorlesungen/2019ss/rn/"
home = "https://uniworx.ifi.lmu.de/"
# sofaproblem

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
                        not ("Correction" in a["href"]) and \
                        (a["href"] != "#"):
                    res["Übung"+str(ix)] = home+a["href"]
                    ix += 1

    return res

# vorlesungen
def get_vorlesungen():
    home = "http://www.nm.ifi.lmu.de/teaching/Vorlesungen/2019ss/rn/"
    page = requests.post(home, verify=False)
    soup = BeautifulSoup(page.text, "html.parser")
    tables = soup.find_all("tbody")
    res = {}
    #print(len(tables))
    for ix,t in enumerate(tables):
        if ix == 0:
            try:
                for ubno, tr in enumerate(t.find_all("tr")):
                    for ix2, cell in enumerate(tr.find_all("td")):
                        if ix2 == 1:
                            title = str(ubno+1)+" "+cell.text
                        elif ix2 == 2:
                            res[title] = home+cell.find_all("a")[1]["href"]
            except:
                res[t.text] = ""
    return res


#v = get_vorlesungen()
#print(v)