import mechanize
from bs4 import BeautifulSoup


def get_tracker():
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    cookies = mechanize.CookieJar()
    browser.set_cookiejar(cookies)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
    browser.set_handle_refresh(False)

    url = "https://www.facebook.com//login/device-based/regular/login/?login_attempt=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.6%2Fdialog%2Foauth%3Fclient_id%3D56912338582%26redirect_uri%3Dhttps%253A%252F%252Fwww.sidereel.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%252Cpublish_actions%252Cuser_friends%26state%3Da3257617fc4596d4b8a7757a9f8b2e3e41fc13789f00dcf9%26ret%3Dlogin%26fallback_redirect_uri%3Db1d0ef11-a990-a0d9-a737-35989172725d&lwv=100"
    browser.open(url)
    browser.select_form(nr = 0)
    browser.form['email'] = "colla69@gmail.com"
    browser.form['pass'] = "COLLA*?!@@123"
    response = browser.submit()
    print(response.read())

    url = "https://www.sidereel.com/tracker"
    response = browser.open(url)
    soup = BeautifulSoup(response.read(), "html.parser")
    links = soup.find_all("ol")
    #print(response.read())
    print(soup.text)

get_tracker()