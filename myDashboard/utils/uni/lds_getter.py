import time
from bs4 import BeautifulSoup
from superDash.psw import uni_psw
import mechanicalsoup


# uebungen
def get_uebungen():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open('https://backstage2auth.pms.ifi.lmu.de:8080/auth/realms/crowdlearning/protocol/openid-connect/auth?client_id=backstage&redirect_uri=https%3A%2F%2Fbackstage2.pms.ifi.lmu.de%3A8080%2Fcourse%2F21310807-3b0c-4482-bb76-cda34eb0430c&state=fb351bb5-081c-42fe-b7f0-cc3d77c223ec&nonce=bb699b11-709b-4524-8006-11ece9a13fef&response_mode=fragment&response_type=code')
    form = browser.select_form('form[class="form-horizontal"]')
    form['username'] = "a.colarieti@campus.lmu.de"
    form['password'] = uni_psw()
    form.print_summary()
    browser.submit_selected()
    browser.open('https://backstage2.pms.ifi.lmu.de:8080/course/21310807-3b0c-4482-bb76-cda34eb0430c')

    while len(browser.get_current_page()) == 3:
        time.sleep(60)
        print(browser.get_current_page())
        continue



# vorlesungen
def get_vorlesungen():
    pass

#get_uebungen()