import mechanicalsoup

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


def get_careerjet_jobs(page):
    browser = mechanicalsoup.StatefulBrowser()
    divs = page.find_all("div", class_="job display-new-job clickable")
    divs.append(page.find("div", class_="job display-new-job clickable first"))
    res = {}
    for div in divs:
        j_link = base_addr + div.find("a", class_="title-company")["href"]

        browser.open(j_link)
        description = browser.get_current_page().find("div", class_="advertise_compact")
        title = div.find("a", class_="title-company").text
        link = j_link

        res[j_link] = {
            "title": title,
            "link": link,
            "description": description,
        }
    return res