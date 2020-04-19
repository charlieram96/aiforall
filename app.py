from flask import Flask, render_template, request, url_for, redirect
import json, pandas as pd 
import matplotlib
import matplotlib.pyplot as plt
#import seaborn as sns

app = Flask(__name__)

@app.route("/login")
def GetData():
    df = pd.read_csv("datasets/results.csv")
    temp = df.to_dict('records')
    columnNames = df.columns.values
    return render_template('record.html', records=temp, colnames=columnNames)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/web_scraper', methods=['GET', 'POST'])
def scraper_page():
    if request.method == "POST":
        product = request.form.get("dataset", None)
        if product == 'Shoes':
            df = pd.read_json("datasets/Shoes.json")
            temp = df.to_dict('records')
            columnNames = df.columns.values
            return render_template('record.html', records=temp, colnames=columnNames, product = product, scroll='scrollDown')
        elif product == 'Pants':
            df = pd.read_json("datasets/Pants.json")
            temp = df.to_dict('records')
            columnNames = df.columns.values
            return render_template('record.html', records=temp, colnames=columnNames, product = product, scroll='scrollDown')
        elif product == 'Shirts':
            df = pd.read_json("datasets/Shirts.json")
            temp = df.to_dict('records')
            columnNames = df.columns.values
            return render_template('record.html', records=temp, colnames=columnNames, product = product, scroll='scrollDown')
        elif product == 'Hats':
            df = pd.read_json("datasets/Hats.json")
            temp = df.to_dict('records')
            columnNames = df.columns.values
            return render_template('record.html', records=temp, colnames=columnNames, product = product, scroll='scrollDown')
    return render_template('record.html')

@app.route('/machine_learning', methods=['GET', 'POST'])
def ml_page():
    model = request.form.get("models", None)
    if model == 'heatmap':
        url_mod = '/static/images/ml_images/heatmap.png'
        mode = 'heatmap'
        return render_template('machine_learning.html', mod=url_mod, mode=mode, scroll='scrollDown')
    if model == 'scatter_1':
        url_mod = '/static/images/ml_images/scatter_positive.png'
        mode = 'scatter_1'
        return render_template('machine_learning.html', mod=url_mod, mode=mode, scroll='scrollDown')
    if model == 'scatter_2':
        url_mod = '/static/images/ml_images/scatter_negative.png'
        mode = 'scatter_2'
        return render_template('machine_learning.html', mod=url_mod, mode=mode, scroll='scrollDown')
    if model == 'scatter_3':
        url_mod = '/static/images/ml_images/scatter_days.png'
        mode = 'scatter_3'
        return render_template('machine_learning.html', mod=url_mod, mode=mode, scroll='scrollDown')
    if model == 'joint_1':
        url_mod = '/static/images/ml_images/jointplot_positive.png'
        mode = 'joint_1'
        return render_template('machine_learning.html', mod=url_mod, mode=mode, scroll='scrollDown')
    if model == 'joint_2':
        url_mod = '/static/images/ml_images/jointplot_negative.png'
        mode = 'joint_2'
        return render_template('machine_learning.html', mod=url_mod, mode=mode, scroll='scrollDown')
    if model == 'joint_3':
        url_mod = '/static/images/ml_images/jointplot_days.png'
        mode = 'joint_3'
        return render_template('machine_learning.html', mod=url_mod, mode=mode, scroll='scrollDown')
    if model == 'pie':
        url_mod = '/static/images/ml_images/pie_chart.png'
        mode = 'pie'
        return render_template('machine_learning.html', mod=url_mod, mode=mode, scroll='scrollDown')

    return render_template('machine_learning.html')

@app.route('/product')
def product_page():

    return render_template('product.html')

@app.route('/guide')
def guide():
    
    return render_template('guide.html')

if __name__ == "__main__":
    app.run(debug=True)