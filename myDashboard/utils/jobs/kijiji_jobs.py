
def get_kiji(soup, time):
    res = {}
    searchres = soup.find("ul", id="search-result")
    for li in searchres.find_all("li"):
        loc = li.find("p", class_="locale")
        if loc is None:
            continue
        a = li.find("a", class_="cta")
        title = a.text.strip()
        link = a["href"]
        description = li.find("p", class_="description").text
        res[link] = {
            "title": title,
            "link": link,
            "description": description,
            "location": loc.text,
            "site": "kijiji",
            "time": time,
        }
    return res


