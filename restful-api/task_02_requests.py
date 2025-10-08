import requests
import csv 

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    posts = response.json()

    def fetch_and_print_posts():
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            posts = response.json()

            for post in posts:
                print(post["title"])
        else:
            print("Error al obtener los posts.")
    
    def fetch_and_save_posts():
        response = requests.get("https://jsonplaceholder.typicode.com/posts")

        if response.status_code == 200:
            posts = response.json()

            filtered_posts = []
            for post in posts:
                filtered_posts.append({
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                })

            with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
                fieldnames = ["id", "title", "body"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()

                writer.writerows(filtered_posts)

            print("Archivo 'posts.csv' creado exitosamente")
        else:
            print(f"Error al obtener los posts. Código de estado: {response.status_code}")
