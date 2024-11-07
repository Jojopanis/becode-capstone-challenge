import requests
import json
from tqdm import tqdm
from time import sleep
from concurrent.futures import ThreadPoolExecutor

def scrap_page(page_number):
    article_list = []
    url_json = f"https://bff-service.rtbf.be/oaos/v1.5/pages/en-continu?_page={page_number}&_limit=100"
    page_json = requests.get(url_json).text
    article_list = json.loads(page_json)["data"]["articles"]
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

def write_json(result, filename='articles.json'):
    data = []
    for r in result:
        data.extend(r)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    with ThreadPoolExecutor() as executor:
        result = executor.map(scrap_page, range(1, 101))
    write_json(result)