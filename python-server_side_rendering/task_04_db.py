#!/usr/bin/python3
from flask import Flask, render_template, request, jsonify
from pathlib import Path
import json
import csv
import sqlite3

# Create an instance for Flask
app = Flask(__name__)
# path to data files
JSON_PATH = 'products.json'
CSV_PATH = 'products.csv'

# read & parse json file function
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# read & parse csv file function
def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items():
    items_list = []

    with open("items.json", 'r') as f:
        rows = json.load(f)
    for key,value in rows.items():
        items_list = value

    return render_template('items.html', items=items_list)

@app.route('/products')
def get_data():
    # Check 'source' query parameter using request args
    source = request.args.get('source')
    id = request.args.get('id')
    if source not in ['json', 'csv']:
        return jsonify({"error": "wrong source"}), 400
    
    # Read data from the corresponding file
    if source == 'json':
        data = read_json(JSON_PATH)
    elif source == 'csv':
        data = read_csv(CSV_PATH)
    elif source == "sql":
        sql_filepath = "products.db"
        if not Path(sql_filepath).is_file():
            create_sql_data(sql_filepath)

        data = load_sql_data(sql_filepath, id)
    
    # Filter data by ID if provided
    if id:
        filtered_data = [item for item in data if str(item['id']) == id]
    else:
        filtered_data = data

    return render_template("product_display.html", data=filtered_data, source=source, id=id)



def load_sql_data(filename, wanted_id = None):
    """ Load SQLite data and return as dictionary """

    data = []
    where_clause = ""
    if wanted_id is not None:
        where_clause = " WHERE id = " + wanted_id

    con = sqlite3.connect(filename)
    cur = con.cursor()
    res = cur.execute("SELECT * FROM products " + where_clause)
    rows = res.fetchall()

    # longwinded way to get a list of the col names programatically
    keys = []
    colnames = cur.description
    for desc in colnames:
        keys.append(desc[0])

    # keys = ["id", "name", "category", "price"]
    for row_tuple in rows:
        item = {}
        i = 0
        for v in row_tuple:
            item[keys[i]] = v
            i = i + 1
        data.append(item)

    # print(data)

    return data

def create_sql_data(filename):
    """ Create SQLite data file if it doesn't already exist """

    con = sqlite3.connect(filename)
    cur = con.cursor()
    cur.execute("CREATE TABLE products(id, name, category, price)")
    cur.execute("""
        INSERT INTO products VALUES
            (1, "Laptop", "Electronics", 799.99),
            (2, "Coffee Mug", "Home Goods", 15.99)
    """)
    con.commit()


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)