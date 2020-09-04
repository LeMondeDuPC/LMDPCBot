from json import dump, load
from feedparser import parse


def get_new_articles():
    links = {"articles": [x["link"].split("https://www.lemondedupc.fr")[1] for x in
                          parse("https://www.lemondedupc.fr/rss.xml").entries]}
    logs = load(open('logs.json'))

    for link in links["articles"]:
        if link not in logs["articles"]:
            newlogs = logs
            newlogs["articles"].insert(0, link)
            dump(newlogs, open('logs.json', 'w'), indent=4)
            return link
        else:
            return ""
