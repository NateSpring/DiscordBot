from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


url = 'https://www.dev.to'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

headlines = soup.find_all('div', class_='crayons-story__indention').a

for headline in headlines:
    link = headline.find('h2', class_='crayons-story__title').a['href']
    print(link)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', news=headlines, link=link)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
