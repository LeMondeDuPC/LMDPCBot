from json import dump
from feedparser import parse

def get_new_articles():
    links = {"articles": [x["link"].split("https://www.lemondedupc.fr")[1] for x in parse("https://www.lemondedupc.fr/rss.xml").entries][:5]}
    dump(links, open('logs.json', 'w'), indent=4)
