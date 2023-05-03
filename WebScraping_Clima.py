import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup

url = 'https://www.dwd.de/DE/wetter/wetterundklima_vorort/hessen/offenbach/_node.html'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
soup

# obtain information from html tag <table>
div_ele = soup.find('div', id='wetklitab')
table = div_ele.find('table')


# obtain information from html tag <tr>

headers = []
for i in table.find_all('tr'):
    title = i.text
    headers.append(title)
    print(f"{title}")