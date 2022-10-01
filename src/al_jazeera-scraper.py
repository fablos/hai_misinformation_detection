import requests
from bs4 import BeautifulSoup

headers = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

#url = 'https://www.aljazeera.com/news/2022/9/30/russia-ukraine-war-list-of-key-events-day-219'
base_url = 'https://www.aljazeera.com'
url = '/news/2022/9/29/russia-ukraine-war-list-of-key-events-day-218'

response = requests.get(base_url+url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

#article_content = soup.find_all('div', {'class':'wysiwyg wysiwyg--all-content css-ibbk12'})


for h in soup.find('ul', {'class':'spaced-bullet-spacing'}):
    print(h.text)
    a = h.find('a')
    try:
        if 'href' in a.attrs:
            c_url = a.get('href')
            print(c_url,' *********** \n')
            c_response = requests.get(base_url + c_url, headers=headers)
            c_soup = BeautifulSoup(c_response, 'html.parser')
            article_content = soup.find('div', {'class': 'wysiwyg wysiwyg--all-content css-ibbk12'})
            print(article_content.text)
            # for p in article_content:
            #     print(p.text)
            #     break
            print(c_url, ' ------------- \n')
    except:
        pass