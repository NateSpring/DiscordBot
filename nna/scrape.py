from bs4 import BeautifulSoup
import requests

def scrape():
    for page in range(0, 3):
        page = page + 1
        base_url = 'https://www.cnet.com/news/'
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, "html.parser")
    headlines = soup.find_all('div', class_='col-2 assetText')
    
    for headline in headlines:
        print(headline.a.text)
scrape()