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
        new_date = date_time.strftime("%d/%m/%Y")
        date_filtered = {"timestamp": new_date}
        news = search_news(date_filtered)

        news_filtered = []
        for new in news:
            news_filtered.append((new["title"], new["url"]))
    except ValueError:
        raise ValueError("Data inválida")

    return news_filtered


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
