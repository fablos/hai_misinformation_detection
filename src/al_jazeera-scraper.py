import requests
from bs4 import BeautifulSoup
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

#url = 'https://www.aljazeera.com/news/2022/9/30/russia-ukraine-war-list-of-key-events-day-219'
BASE_URL = 'https://www.aljazeera.com'
url = '/news/2022/9/29/russia-ukraine-war-list-of-key-events-day-218'


def get_article(url='', base_url=BASE_URL, headers=HEADERS):
    response = requests.get(base_url + url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    article_content = soup.find('div', {'class': 'wysiwyg wysiwyg--all-content css-ibbk12'})
    return '\n'.join([p.text for p in BeautifulSoup(str(article_content), 'html.parser').findAll('p')])


def get_key_points(url='', base_url=BASE_URL, headers=HEADERS):
    response = requests.get(base_url + url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    for h in soup.find('ul', {'class': 'spaced-bullet-spacing'}):
        if len(h.text) > 1:
            print(h.text, '\n')
            s2 = BeautifulSoup(str(h), 'html.parser')
            for link in s2.findAll('a'):
                print(link.get('href'))
                article = get_article(url=link.get('href'))
                print(article)
                print('ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo')
            break

get_key_points(url=url)