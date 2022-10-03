from src.al_jazeera_scraper import get_key_points
import re
import json
import time
from os.path import exists


def extract_date(url):
    m = re.search(r"[0-9]{4}/[0-9]{1,2}/[0-9]{1,2}", url)
    return m.group(0)


with open('links.txt', encoding='utf-8') as f:
    links = f.read().splitlines()

data = json.load(open('data.json')) if exists('data.json') else {}

assert len(data.keys()) > 0

for link in links[:22]:
    d = extract_date(link)
    if d not in data.keys():
        data[d] = get_key_points(link)
        time.sleep(5)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
