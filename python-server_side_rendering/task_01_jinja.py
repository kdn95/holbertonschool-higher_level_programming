#!/usr/bin/python3
"""Basic Flask App"""
from flask import Flask, render_template
# Create an instance for Flask
app = Flask(__name__)
# Create home page


@app.route('/')
def home():
    """ Use render_template function to return index.html """
    return render_template('index.html')


@app.route('/about')
def about():
    """ Use render_template function to return about.html """
    return render_template('about.html')


@app.route('/contact')
def contact():
    """ Use render_template function to return contact.html """
    return render_template('contact.html')


# Conditional check if script is being directly executed
if __name__ == '__main__':
    app.run(debug=True, port=5000)
