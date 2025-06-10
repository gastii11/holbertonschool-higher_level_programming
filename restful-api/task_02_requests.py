#!/usr/bin/python3
import requests
import csv


def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()

        simplified_posts = []
        for post in posts:
            simplified_posts.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })

        with open('post.csv', mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(simplified_posts)
