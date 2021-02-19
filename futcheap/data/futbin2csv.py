import requests
import tqdm
import csv
import re
from bs4 import BeautifulSoup
import time


FUTBIN_PLAYERS_URL = 'https://www.futbin.com/21/players'
REQUEST_HEADERS = {
    'User-Agent': """Mozilla/5.1 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"""
}

num_pages = 660

COLUMNS = [
    'club',
    'nation',
    'league',
    'name',
    'rating',
    'position',
    'price',
    'card_types'
]

with open('data_660.csv', 'w') as f:
    csv_writer = csv.DictWriter(f, fieldnames=COLUMNS)
    csv_writer.writeheader()
    for page in tqdm.tqdm(range(1, num_pages + 1)):
        players_page_content = requests.get(
            FUTBIN_PLAYERS_URL + f"?page={page}",
            headers=REQUEST_HEADERS
        )
        bs = BeautifulSoup(players_page_content.text, 'html.parser')
        table = (bs.find('table', {'id': 'repTb'}))
        tbody = table.find('tbody')
        extracted = tbody.findAll('tr', {'class': re.compile(r'player_tr_\d+')})

        for content in extracted:
            player = {}
            divs = content.find_all("a")
            player['club'] =   divs[1]['data-original-title']
            player['nation'] = divs[2]['data-original-title']
            player['league'] = divs[3]['data-original-title']
            tds = content.find_all("td")
            player['name'] = tds[0].text.strip()
            player['rating'] = tds[1].text.strip()
            player['position'] = tds[2].text.strip()
            player['price'] = tds[4].text.strip()
            player['card_types'] = " ".join(content.find('img')['class'][6:])
            csv_writer.writerow(player)
        time.sleep(5)
