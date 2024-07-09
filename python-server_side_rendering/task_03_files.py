#!/usr/bin/python3
"""Basic Flask App"""
from flask import Flask, render_template, jsonify, request
import csv
import json
import os

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
# Create home page
@app.route('/')
def home():
    """ Use render_template function to return index.html """
    return render_template('index.html')

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
    
    # Filter data by ID if provided
    if id:
        filtered_data = [item for item in data if str(item['id']) == id]
    else:
        filtered_data = data

    return render_template("product_display.html", data=filtered_data, source=source, id=id)


# Conditional check if script is being directly executed
if __name__ == '__main__':
    app.run(debug=True, port=5000)
