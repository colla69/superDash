from superDash.psw import uni_psw
import mechanicalsoup

# uebungen
def get_uebungen():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open('https://uni2work.ifi.lmu.de')
    browser.follow_link("login")
    # print(browser.get_current_page())
    form = browser.select_form('form[action="https://uni2work.ifi.lmu.de/auth/page/LDAP"]')
    form['f1'] = "a.colarieti@campus.lmu.de"
    form['f2'] = uni_psw()
    form.print_summary()
    resp = browser.submit_selected()

    browser.open('https://uni2work.ifi.lmu.de/course/S19/IfI/ProMo/ex')

    #res = { browser.get_current_page()}

    return browser.get_current_page()


ub = get_uebungen()
print(ub)