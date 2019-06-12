
def get_kiji(soup, time):
    res = {}
    searchres = soup.find("ul", id="search-result")
    for li in searchres.find_all("li"):
        loc = li.find("p", class_="locale")
        if loc is None:
            continue
        if True: # loc.text.lower() == "bologna":
            title = li.find("a", class_="cta").text.strip()
            link = li.find("a", class_="cta")["href"]
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


