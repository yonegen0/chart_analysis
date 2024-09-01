from flask import Flask, render_template, request
from wtforms import IntegerField, SubmitField, DateField
from wtforms.form import Form

import my_flask.chart_analysis as chart

app = Flask(__name__, static_folder="my_flask")

class StockInfForm(Form):
    stockCode = IntegerField('銘柄コード')
    enterButton = SubmitField('検索')
    startDay = DateField('分析開始日')
    finishDay = DateField('分析終了日')

@app.route('/', methods=["GET", "POST"])
def stock_form():
    stockForm = StockInfForm(request.form)
    if request.method == "POST":
        if stockForm.validate():
            stockCode = stockForm.stockCode.data
            startDay = stockForm.startDay.data
            finishDay = stockForm.finishDay.data
            stockForm = StockInfForm()
        else:
            print('入力に誤りがあります')
    return render_template('form.html', form=stockForm)

@app.route('/index')
def index():
    chart.chart_view()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)