import os
from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# =========================
# Health check (Kubernetes)
# =========================
@app.route("/sante")
def sante():
    return "OK", 200

# =========================
# MongoDB Connection
# =========================
MONGO_URI = os.environ.get(
    "MONGO_URI",
    "mongodb://localhost:27017/"
)

client = MongoClient(MONGO_URI)
db = client["inventory"]
collection = db["computers"]

# =========================
# Seed Data
# =========================
initial_computers = [
    {"name": "Dell Latitude 5540", "category": "Laptop", "stock": 12, "price": 1200},
    {"name": "HP EliteBook 840 G11", "category": "Laptop", "stock": 8, "price": 1400},
    {"name": "Lenovo ThinkCentre M90", "category": "Desktop", "stock": 5, "price": 950},
    {"name": "MacBook Pro M4", "category": "Laptop", "stock": 3, "price": 2600},
    {"name": "Dell OptiPlex 7010", "category": "Desktop", "stock": 15, "price": 1100},
    {"name": "Lenovo ThinkPad X1 Carbon", "category": "Laptop", "stock": 6, "price": 2200},
    {"name": "HP ProDesk 600 G9", "category": "Desktop", "stock": 10, "price": 1050},
    {"name": "Apple iMac 24", "category": "Desktop", "stock": 2, "price": 2400},
    {"name": "Microsoft Surface Laptop 7", "category": "Laptop", "stock": 7, "price": 1900},
    {"name": "ASUS ExpertBook B5", "category": "Laptop", "stock": 4, "price": 1600},
]

# Auto-seed
if collection.count_documents({}) == 0:
    collection.insert_many(initial_computers)

# =========================
# HOME
# =========================
@app.route("/")
def home():

    query = request.args.get("q")
    category = request.args.get("category")

    mongo_filter = {}

    if query:
        mongo_filter["name"] = {"$regex": query, "$options": "i"}

    if category:
        mongo_filter["category"] = category

    computers = list(collection.find(mongo_filter, {"_id": 0}))

    total_products = len(computers)
    total_stock = sum(c["stock"] for c in computers)
    inventory_value = sum(c["stock"] * c["price"] for c in computers)

    return render_template(
        "index.html",
        computers=computers,
        total_products=total_products,
        total_stock=total_stock,
        inventory_value=inventory_value,
        query=query,
        category=category
    )

# =========================
# ADD PRODUCT
# =========================
@app.route("/add", methods=["POST"])
def add():

    new_item = {
        "name": request.form["name"],
        "category": request.form["category"],
        "stock": int(request.form["stock"]),
        "price": float(request.form["price"])
    }

    collection.insert_one(new_item)

    return redirect("/")

# =========================
# RUN
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)