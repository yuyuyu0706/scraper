from bs4 import BeautifulSoup
import requests
res = requests.get('https://xxxx.co.jp')
soup = BeautifulSoup(res.text, 'html.parser')

for a in soup.find_all('a'):
    print(a.text)
