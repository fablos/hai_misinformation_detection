import requests
from bs4 import BeautifulSoup

headers = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

#url = 'https://www.aljazeera.com/news/2022/9/30/russia-ukraine-war-list-of-key-events-day-219'
url = 'https://www.aljazeera.com/news/2022/9/29/russia-ukraine-war-list-of-key-events-day-218'

response = requests.get(url, headers=headers)

#print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

#content = soup.find_all('div', {'class':'wysiwyg wysiwyg--all-content css-ibbk12'})
content = soup.find('ul', {'class':'spaced-bullet-spacing'})

#print(content)

#for el in content:
#    link = el.find('a')
#    print(el, link,'****************************')

content = soup.find('ul', {'class':'spaced-bullet-spacing'})

for h in soup.find('ul', {'class':'spaced-bullet-spacing'}):
    print(h.text)
    a = h.find('a')
    try:
        if 'href' in a.attrs:
            url = a.get('href')
            print(a.text, url)
    except:
        pass