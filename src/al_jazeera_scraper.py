import requests
from bs4 import BeautifulSoup
from keybert import KeyBERT

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

BASE_URL = 'https://www.aljazeera.com'


def get_article(url='', base_url=BASE_URL, headers=HEADERS):
    print('Article --> '+url)
    response = requests.get(base_url + url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('h1')
    article_content = soup.find('div', {'class': 'wysiwyg wysiwyg--all-content css-ibbk12'})
    return title.text, '\n'.join([p.text for p in BeautifulSoup(str(article_content), 'html.parser').findAll('p')])


def get_key_points(url='', headers=HEADERS):
    print(url)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    events = []
    kw_model = KeyBERT()
    event_list = soup.find('ul', {'class': 'spaced-bullet-spacing'})
    if event_list:
        for h in event_list:
            if len(h.text) > 1:
                o = {'short_text': h.text, 'articles': []}
                s2 = BeautifulSoup(str(h), 'html.parser')
                for link in s2.findAll('a'):
                    url = link.get('href')
                    if url.startswith('/news/'):
                        title, article = get_article(url=url)
                        o['articles'].append({'title': title, 'body': article, 'keywords': kw_model.extract_keywords(article)})
                events.append(o)
    return events

def simple_test():
    url = '/news/2022/9/29/russia-ukraine-war-list-of-key-events-day-218'
    events = get_key_points(url=url)
    for e in events:
        print(e['short_text'])
        if len(e['articles']) > 0:
            for a in e['articles']:
                print(a['keywords'])
        print('\n ****************************** \n')