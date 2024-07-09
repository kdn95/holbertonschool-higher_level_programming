#!/usr/bin/python3
"""Basic Flask App"""
from flask import Flask, render_template
import json
# Create an instance for Flask
app = Flask(__name__)

# Create home page
@app.route('/')
def home():
    """ Use render_template function to return index.html """
    return render_template('index.html')

@app.route('/items')
def items():
    # open JSON file
    with open('items.json', 'r') as f:
        # load json obj as dict
        data = json.load(f)
        p_items = data['items']
    return render_template("items.html", items=p_items)


# Conditional check if script is being directly executed
if __name__ == '__main__':
    app.run(debug=True, port=5000)
