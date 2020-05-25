from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


url = 'https://www.dev.to'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

#title = soup.find_all('h2', class_='crayons-story__title')

headlines = soup.find_all('div', class_='crayons-story__indention')

for headline in headlines:
    titles = headline.find('a')
    links = headline.find('a')['href']
    print(titles)

#for item, links in zip(title, link): 
#    print(item, links)


app = Flask(__name__)

app.jinja_env.globals.update(zip=zip)

@app.route('/')
def index():
    return render_template('index.html', titles=titles, links=links)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
