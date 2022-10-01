import requests

source = 'https://www.nytimes.com/article/ukraine-russia-war-timeline.html'

headers = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

response = requests.get(source, headers=headers)

print(response)
