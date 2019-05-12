from bs4 import BeautifulSoup
from superDash.psw import uni_psw
import mechanicalsoup

# uebungen
def get_uebungen():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open('https://uni2work.ifi.lmu.de')
    browser.follow_link("login")
    form = browser.select_form('form[action="https://uni2work.ifi.lmu.de/auth/page/LDAP"]')
    form['f1'] = "a.colarieti@campus.lmu.de"
    form['f2'] = uni_psw()
    # form.print_summary()
    browser.submit_selected()
    browser.open('https://uni2work.ifi.lmu.de/course/S19/IfI/ProMo/ex')
    page = browser.get_current_page()
    uebungen = []
    table = page.find_all("td")
    for td in table:
        if "blatt" in td.text.lower():
            uebungen.append(td.find("a")["href"])
    pages = []
    for ub in uebungen:
        browser.open(ub)
        pages.append(browser.get_current_page())
    res = {}
    for p in reversed(pages):
        for td in p.find_all("td"):
            if ".pdf" in td.text.lower():
                res[td.text] = td.find("a")["href"]
    return res


def get_vorlesungen():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open('https://uni2work.ifi.lmu.de')
    browser.follow_link("login")
    form = browser.select_form('form[action="https://uni2work.ifi.lmu.de/auth/page/LDAP"]')
    form['f1'] = "a.colarieti@campus.lmu.de"
    form['f2'] = uni_psw()
    # form.print_summary()
    browser.submit_selected()
    browser.open('https://uni2work.ifi.lmu.de/course/S19/IfI/ProMo/file')
    page = browser.get_current_page()
    res = {}
    for tr in page.find_all("tr"):
        for ix, td in  enumerate(tr.find_all("td")):
            if ix == 1:
                titel = td.text
            if ix == 3:
                if "kapitel" in titel.lower():
                    res[titel] = td.find("a")["href"]
    return res



#ub = get_vorlesungen()
#print(ub)
