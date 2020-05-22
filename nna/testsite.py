from flask import Flask, render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('gitlog430.csv')
data.columns = ["Author", "Day", "Date", "Message", " ", " "]
df = data[['Day', 'Date', 'Message']]


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
