from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


url = 'https://www.dev.to'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

titles = soup.find_all('h2', class_='crayons-story__title')


links = []
for title in titles:
    link = title.find('a')['href']
    links.append(link)



app = Flask(__name__)

app.jinja_env.globals.update(zip=zip)

@app.route('/')
def index():
    return render_template('index.html', len = len(titles), titles=titles, links=links)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
