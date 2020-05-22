import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.indiehackers.com/products?sorting=highest-revenue')
soup = BeautifulSoup(r.content, 'html5lib')

headings = soup.find_all('article', {'class': 'Card-sc-4llv5q-0 fkexff'})
for heading in headings:
    print(heading.a.text)