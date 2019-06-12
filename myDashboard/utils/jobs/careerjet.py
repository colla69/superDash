import mechanicalsoup
from myDashboard.models import DataDump
from bs4 import BeautifulSoup

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
    base_addr = "https://www.careerjet.it"
    divs = soup.find_all("div", class_="job display-new-job clickable")
    divs.append(soup.find("div", class_="job display-new-job clickable first"))
    res = {}
    for div in divs:
        title = div.find("a", class_="title-company").text
        j_link = base_addr + div.find("a", class_="title-company")["href"]
        description, location = get_single_careerinfo(j_link)
        res[j_link] = {
            "title": title,
            "link": j_link,
            "description": description,
            "location": location,
            "site": "careerjet.it",
            "time": time,
        }
    return res


def get_single_careerinfo(j_link):
    single_job = DataDump.objects.all().filter(source=j_link)
    for sj in single_job:
        page = BeautifulSoup(sj.data, "html.parser")
        description = page.find("div", class_="advertise_compact").text
        link = j_link
        location = page.find("div",class_="locations_compact").text
        return description, location
