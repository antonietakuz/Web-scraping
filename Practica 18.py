#pip install requests
#pip install beautifulsoup4
#python -m pip install --upgrade pip

import requests
from bs4 import BeautifulSoup

url = "https://tugalaxiaartesanal.empretienda.com.ar/productos"

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
}

req = requests.get(url, headers=headers)

# req = requests.get(url)

#print(req)
soup = BeautifulSoup(req.content, 'html.parser')
#print(soup)
lista = soup.select(".products-feed__product-wrapper")

for item in lista:
  print(item.select_one(".products-feed__product-name.text--primary").get_text())
  print(item.select_one(".products-feed__product-price.text--primary").get_text())