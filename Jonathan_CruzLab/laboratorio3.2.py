import requests

def get_posts():
    """Obtiene posts desde JSONPlaceholder"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        return sorted(response.json(), key=lambda x: x["id"])
    else:
        raise Exception(f"Error al obtener posts: {response.status_code}")

def binary_search_posts(posts, target_id):
    """Busca un post por ID usando búsqueda binaria"""
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

# Uso correcto
if __name__ == "__main__":
    try:
        posts = get_posts()
        target_post = binary_search_posts(posts, 42)
        
        if target_post:
            print(f"Post encontrado:\nID: {target_post['id']}\nTítulo: {target_post['title']}")
        else:
            print("Post no encontrado")
            
    except Exception as e:
        print(f"Error: {e}")