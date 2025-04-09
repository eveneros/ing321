import requests

def get_starwars_characters():
    url = "https://swapi.dev/api/people/"
    response = requests.get(url)
    return response.json()["results"]

def create_hash_table(characters):
    return {characters["name"]: characters for characters in characters}

characters = get_starwars_characters()
hash_table = create_hash_table(characters)

def search_characters(name):
    return hash_table.get(name, "personaje no encontrado")

print(search_characters("Darth Vader"))