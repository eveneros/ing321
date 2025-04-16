import requests

def get_starwars_characters():
    url = "https://swapi.dev/api/people/"
    response = requests.get(url)
    return response.json()["results"]  # Lista de personajes

def create_hash_table(characters):
    return {character["name"]: character for character in characters}

# Uso:
characters = get_starwars_characters()
hash_table = create_hash_table(characters)

def search_character(name):
    return hash_table.get(name, "Personaje no encontrado")

# Ejemplo:
print(search_character("Luke Skywalker"))  # Devuelve todos los datos de Luke