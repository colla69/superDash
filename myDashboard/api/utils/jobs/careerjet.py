import mechanicalsoup
from bs4 import BeautifulSoup

from myDashboard.models import DataDump

base_addr = "https://www.careerjet.it"


def get_careerjet_single_links(link):
    res = []
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(link)
    page = browser.get_current_page()
    divs = page.find_all("div", class_="job display-new-job clickable")
    divs.append(page.find("div", class_="job display-new-job clickable first"))
    for div in divs:
        res.append(base_addr + div.find("a", class_="title-company")["href"])
    return res


def get_careerjet_jobs(soup, time):
    global data
    data = DataDump.objects.all()
    divs = soup.find_all("div", class_="job display-new-job clickable")
    divs.append(soup.find("div", class_="job display-new-job clickable first"))
    res = {}
    for div in divs:
        try:
            title_div = div.find("a", class_="title-company")
            j_link = base_addr + title_div["href"]
            if not j_link in res.keys():
                title = title_div.text
                description, location = get_single_careerinfo(j_link)
                res[j_link] = {
                    "title": title,
                    "link": j_link,
                    "description": description,
                    "location": location,
                    "site": "careerjet.it",
                    "time": time,
                }
        except:
            continue
    return res


def get_single_careerinfo(j_link):
    sj = data.defer("data").filter(source=j_link).order_by("-time")
    for single_job in sj:
        page = BeautifulSoup(single_job.data, "html.parser")
        description = page.find("div", class_="advertise_compact").text
        location = page.find("div",class_="locations_compact").text
        return description, location
