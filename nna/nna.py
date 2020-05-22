from flask import Flask, render_template




app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
