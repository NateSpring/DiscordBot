from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


url = 'https://www.dev.to'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

headlines = soup.find('div', class_='crayons-story__title')
link = headlines.find('a')
for allLinks in link:
    print(link)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', news=headlines)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
