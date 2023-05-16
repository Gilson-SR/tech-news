import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        response.raise_for_status()
        return response.text
    except Exception:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    links = selector.css("h2.entry-title a::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    page_next = selector.css('a.next::attr(href)').get()
    return page_next


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css("h1::text").get().strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author > a::text").get()
    reading_time = int(
        selector.css(".meta-reading-time::text").get().split(" ")[0]
    )
    summary = "".join(
            selector.css(".entry-content > p:nth-of-type(1) *::text").getall()
        ).strip()
    category = selector.css(".category-style .label::text").get()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    links = []
    news = []

    while len(links) < amount:
        html = fetch(url)
        url = scrape_next_page_link(html)
        links.extend(scrape_updates(html))

    for link in links[:amount]:
        content = fetch(link)
        data = scrape_news(content)
        news.append(data)

    create_news(news)
    return news
