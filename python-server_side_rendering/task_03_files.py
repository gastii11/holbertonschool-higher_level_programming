from flask import Flask, render_template, request
from reader import read_products_from_json, read_products_from_csv
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    items = []
    try:
        with open('items.json') as f:
            data = json.load(f)
            items = data.get("items", [])
    except Exception as e:
        print("Error al leer items.json:", e)
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error_message = None
    data = []

    if source == 'json':
        data = read_products_from_json('products.json')
    elif source == 'csv':
        data = read_products_from_csv('products.csv')
    else:
        error_message = "Wrong source. Please use 'json' or 'csv'."
        return render_template('product_display.html', products=[], error=error_message)

    if product_id:
        try:
            pid = int(product_id)
            data = [item for item in data if int(item["id"]) == pid]
            if not data:
                error_message = f"Product with ID {pid} not found."
        except ValueError:
            error_message = "Invalid ID. It must be a number."
            data = []

    return render_template('product_display.html', products=data, error=error_message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
