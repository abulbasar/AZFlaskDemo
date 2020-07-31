import requests
from xml.etree import ElementTree as et


def load_rss_feed():
    url = "https://www.zdnet.com/news/rss.xml"
    response = requests.get(url)
    root = et.fromstring(response.text)
    docs = []
    for item in root.findall("*/item"):
        doc = dict(
            guid=item.find("guid").text,
            link=item.find("link").text,
            title=item.find("title").text,
            description=item.find("description").text,
            pub_date=item.find("pubDate").text
        )
        docs.append(doc)
    return docs