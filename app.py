from my_flask import app
from flask import Flask, render_template

import my_flask.chart_analysis as chart

app = Flask(__name__, static_folder="my_flask")

@app.route('/')
def index():
    chart.chart_view()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)