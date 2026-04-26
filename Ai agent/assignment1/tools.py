import requests
from bs4 import BeautifulSoup

def search_web(query):
    # Simple DuckDuckGo search
    url = f"https://duckduckgo.com/html/?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = []
    for a in soup.find_all("a", class_="result__a", href=True):
        links.append(a["href"])

    return links[:3]


def scrape_page(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = [p.get_text() for p in soup.find_all("p")]
        text = " ".join(paragraphs)

        return text[:2000]  # limit
    except:
        return ""