import requests
def get_starwars_characters():
    url = "https://swapi.dev/api/people/"
    response = requests.get(url)
    return response.json()["results"] #lista de personajes

#crear tabla de hash (diccionario)para la busqueda rapida

def create_hash_table(characters):
    return{character["name"]: character for character in characters}

#uso
characters = get_starwars_characters()
hash_table = create_hash_table(characters)

def search_character(name):
    return hash_table.get(name, "personaje no encontrado")

print(search_character("Luke Skywalker"))

