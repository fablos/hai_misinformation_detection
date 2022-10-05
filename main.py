#
# Copyright (C) 2022  Fabrizio Lo Scudo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from src.al_jazeera_scraper import get_key_points
import re
import json
import time
from os.path import exists

from src.links_creator import generate_link_list


def extract_date(url):
    m = re.search(r"[0-9]{4}/[0-9]{1,2}/[0-9]{1,2}", url)
    return m.group(0)

generate_link_list()

with open('links.txt', encoding='utf-8') as f:
    links = f.read().splitlines()

data = json.load(open('data.json', encoding='utf-8')) if exists('data.json') else {}

assert len(data.keys()) > 0

for link in links:
    d = extract_date(link)
    if d not in data.keys():
        data[d] = get_key_points(link)
        time.sleep(5)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
