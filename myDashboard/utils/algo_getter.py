from lxml import html
import requests
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_data(self, data):
        if data != "":
            print("Encountered some data  :", data)


page = requests.get('http://www.dbs.ifi.lmu.de/cms/studium_lehre/lehre_bachelor/algodat19/index.html')
tree = html.fromstring(page.content)

parser = MyHTMLParser()
parser.feed(page.text)
