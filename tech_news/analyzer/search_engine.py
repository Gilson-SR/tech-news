from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    if news:
        return [(new["title"], new["url"]) for new in news]
    return []


# Requisito 8
def search_by_date(date):
    try:
        date_time = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    format_date = "{:%d/%m/%Y}".format(date_time)
    news = search_news({"timestamp": format_date})
    return list(news)


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
