from bs4 import BeautifulSoup as BS
import requests
from django.views.decorators.csrf import csrf_exempt

URL = 'https://faberlic.com'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.931 YaBrowser/23.9.3.931 Yowser/2.5 Safari/537.36",
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all("div", class_="cardWrapper")
    faberlic_products = []

    for item in items:
        faberlic_products.append(
            {
                'title_name': item.find("h3", class_="cardTitle").get_text(),
                'price': item.find("p", class_="cardPrice cardPriceSale cardPriceSaleRed").get_text(),
                'title_url': URL + item.find("a").get("href"),
                'image': item.find("div", class_="imgReplace").find("img").get("src"),
            }
        )
    return faberlic_products

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        all_products = []
        for page in range(0, 1):
            html = get_html(f'https://faberlic.com/index.php?option=com_catalog&view=listgoods&idcategory=1000175334690&Itemid=2075&lang=ru', params=page)
            all_products.extend(get_data(html.text))
            return all_products
    else:
        raise Exception('Error parsing ❗️😥')