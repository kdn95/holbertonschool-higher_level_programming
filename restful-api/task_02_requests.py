#!/usr/bin/python3
"""Using Request Library"""
import csv
import requests


def fetch_and_print_posts():
    """
    Function to fetch
    all posts from JSONPlaceholder
    """
    link = 'https://jsonplaceholder.typicode.com/posts/'
    try:
        r = requests.get(link)
        print("Status Code: {}".format(r.status_code))
        
        if r.status_code == 200:
            f_data = r.json()

            for data in f_data:
                print(data['title'])
        else:
            print("Fetch posts fail")
    except Exception as excep:
        print("Error occurred: {}".format(excep))


def fetch_and_save_posts():
    """
    Fetch all posts from JSON
    """
    link = 'https://jsonplaceholder.typicode.com/posts/'
    resp = requests.get(link, timeout=10)

    if resp.status_code == 200:
        post = resp.json()

        struct_d = []
        for data in post:
            struct_d.append({
                'id': data['id'], 
                'title': data['title'], 
                'body':data['body']
            })
        csv_f = 'posts.csv'
        with open(csv_f, "w", encoding='utf-8') as csv_file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csv_file,
                                    fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(struct_d)
