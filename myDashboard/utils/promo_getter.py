from lxml import html
import requests
from bs4 import BeautifulSoup
from superDash.psw import uni_psw

# uebungen
def get_uebungen():
    payload = {'hident11': "a.colarieti@campus.lmu.de", 'hident12': uni_psw()}
    session = requests.Session()
    r = session.post("https://uni2work.ifi.lmu.de/")
    cookies = dict(r.cookies)
    headers = dict(r.headers)

    csrftoken = cookies['XSRF-TOKEN']
    headers['X-XSRF-TOKEN'] = csrftoken
    headers['ContentType'] = "application/x-www-form-urlencoded"

    login = session.post("https://uni2work.ifi.lmu.de/auth/page/LDAP", data=payload, headers=session.headers, cookies=session.cookies)
    print("login  "+str(login.status_code))

    csrftoken = cookies['XSRF-TOKEN']
    headers['X-XSRF-TOKEN'] = csrftoken

    page = session.get("https://uni2work.ifi.lmu.de/course/S19/IfI/ProMo/ex", headers=session.headers, cookies=session.cookies)

    res = {}

    return res


ub = get_uebungen()
print(ub)