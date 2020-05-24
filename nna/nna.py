from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


url = 'https://www.cnet.com/news/'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
headlines = soup.find_all('div', class_='col-2 assetText')
news = {}
for headline in headlines:
    news[header] = news.append(headline.text)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', news=news)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
