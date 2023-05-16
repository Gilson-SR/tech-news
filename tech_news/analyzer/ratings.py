from tech_news.database import search_news
from collections import Counter


# Requisito 10
def top_5_categories():
    news = search_news({})
    categories = [new["category"] for new in news]
    counter = Counter(categories).most_common(5)
    sorted_categories = sorted(counter, key=lambda x: (-x[1], x[0]))
    return [category[0] for category in sorted_categories]
