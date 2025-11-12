from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    with open("products.json", "r") as f:
        return json.load(f)

def read_csv():
    products = []
    with open("products.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

@app.route("/products")
def show_products():
    source = request.args.get("source")
    product_id = request.args.get("id")
    products = []
    error = None

    # Validar fuente
    if source == "json":
        products = read_json()
    elif source == "csv":
        products = read_csv()
    else:
        error = "Wrong source"
        return render_template("product_display.html", error=error)

    # Filtrar por id si existe
    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in products if p["id"] == product_id]
            if not filtered:
                error = "Product not found"
            products = filtered
        except ValueError:
            error = "Invalid id format"

    return render_template("product_display.html", products=products, error=error)

if __name__ == "__main__":
    app.run(debug=True)
