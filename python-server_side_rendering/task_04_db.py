from flask import Flask, request, render_template
import json
import csv
import sqlite3

app = Flask(__name__)

def get_from_sql(id=None):
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        if id:
            cursor.execute("SELECT * FROM Products WHERE id = ?", (id,))
        else:
            cursor.execute("SELECT * FROM Products")

        rows = cursor.fetchall()
        conn.close()

        products = [
            {"id": r[0], "name": r[1], "category": r[2], "price": r[3]}
            for r in rows
        ]
        return products
    except Exception as e:
        return {"error": str(e)}

@app.route('/products')
def products():
    source = request.args.get("source", "json")
    product_id = request.args.get("id", None)

    if product_id:
        try:
            product_id = int(product_id)
        except:
            return "Invalid id"

    if source == "json":
        with open("products.json") as f:
            data = json.load(f)
        products = data if not product_id else [p for p in data if p["id"] == product_id]

    elif source == "csv":
        with open("products.csv") as f:
            reader = csv.DictReader(f)
            data = list(reader)

        for p in data:
            p["id"] = int(p["id"])
            p["price"] = float(p["price"])

        products = data if not product_id else [p for p in data if p["id"] == product_id]

    elif source == "sql":
        products = get_from_sql(product_id)

        if isinstance(products, dict) and "error" in products:
            return f"Database error: {products['error']}"

    else:
        return "Wrong source"

    return render_template("product_display.html", products=products)

# 🔥 ESTA PARTE FALTABA
if __name__ == '__main__':
    app.run(debug=False)
