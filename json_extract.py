import requests
import json

def cycle_pages(number_of_pages):
    all_articles = []
    for i in range(number_of_pages):
        url_json = f"https://bff-service.rtbf.be/oaos/v1.5/pages/en-continu?_page={i+1}&_limit=100"
        page_json = requests.get(url_json).text
        print(f"Scraping page {i+1}...")
        article_list = json.loads(page_json)["data"]["articles"]
        all_articles.extend(scrap_page(article_list))
    return all_articles

def scrap_page(article_list):
    data_articles = []
    for article in article_list:
        article_data = {
            "id": article["id"],
            "slug": article["slug"],
            "title": article["title"],
            "category": article["dossierLabel"],
            "date": article["publishedFrom"]}
        data_articles.append(article_data)
    return data_articles

if __name__ == "__main__":
    with open('articles.json', 'w') as f:
        json.dump(cycle_pages(100), f, indent=2)
    