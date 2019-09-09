import mechanicalsoup
from django.utils import timezone

from myDashboard.models import DataDump

login = "https://www.linkedin.com/uas/login?emailAddress=&fromSignIn=&trk=guest_job_search_nav-header-signin"
link = "https://www.linkedin.com/jobs/search/?distance=25&f_F=it%2Ceng&location=Bologna%2C%20Emilia-Romagna%2C%20Italy&locationId=PLACES.it.5-1-215&sortBy=DD"


def get_linkedin_jobs(soup, time, link):
    res = {}
    try:
        title = soup.find("h1").text
    except:
        return res
        title = ""
    description = soup.find("div", class_="description__text").text
    location = soup.find("span", class_="topbar__company-info-meta").text
    res[link] = {
        "title": title,
        "link": link,
        "description": description,
        "location": location,
        "site": "linkedin.it",
        "time": time,
    }
    return res


def save_linkedin():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(login)
    page = browser.get_current_page()
    form = browser.select_form(nr=0)
    # form.print_summary()
    form['fp_data'] = "huhu"
    form['session_password'] = "hu"
    response = browser.submit_selected()
    browser.open(link)
    page = browser.get_current_page()
    li_list = page.find_all("li", class_="result-card")
    for li in li_list:
        job_link = li.find("a", class_="result-card__full-card-link")["href"]
        browser.open(job_link)
        job_page = browser.get_current_page()
        DataDump.objects.create(
            time=timezone.now(),
            source=job_link,
            data=str(job_page).encode("utf-8")
        )
        # print(job_page)
