import asyncio
import json

from bs4 import BeautifulSoup
import requests


async def get_new_articles():
    page = requests.get("https://www.lemondedupc.fr/")
    soup = BeautifulSoup(page.content, features="lxml")
    logs = json.load(open('logs.json'))

    for article in soup.find_all("article", class_="mini-post"):
        link = article.find("a", href=True)['href']
        if "article" in link and link not in logs["articles"]:
            newlogs = logs
            newlogs["articles"].append(link)
            json.dump(newlogs, open('logs.json', 'w'), indent=4)
            return link
    return ""
