import requests

def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    posts = response.json()
    return sorted(posts, key=lambda x: x["id"])  # Ordenar por ID

# Ejemplo de datos: [{"id": 1, "title": "...", "userId": 1}, ...]

def binary_search_posts(posts, target_id):
    left, right = 0, len(posts) - 1
    while left <= right:
        mid = (left + right) // 2
        if posts[mid]["id"] == target_id:
            return posts[mid]
        elif posts[mid]["id"] < target_id:
            left = mid + 1
        else:
            right = mid - 1
    return None

# Uso:
posts = get_posts()
target_post = binary_search_posts(posts, 42)  # Buscar post con ID=42
print(target_post)