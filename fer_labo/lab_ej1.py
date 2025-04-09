import requests

def obtener_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    respuesta = requests.get(url)
    posts = respuesta.json()
    return sorted(posts, key=lambda post: post["id"])  # Ordenar por ID

def busqueda_binaria(posts, id_objetivo):
    izquierda = 0
    derecha = len(posts) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        id_actual = posts[medio]["id"]

        if id_actual == id_objetivo:
            return posts[medio]
        elif id_actual < id_objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None 


posts = obtener_posts()
post_encontrado = busqueda_binaria(posts, 42) 


if post_encontrado:
    print("Post encontrado:")
    print(post_encontrado)
else:
    print("No se encontró un post con ese ID.")