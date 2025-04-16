import requests

def obtener_personajes_starwars():
    """
    Consulta la API de Star Wars y devuelve una lista de personajes.
    """
    url = "https://swapi.dev/api/people/"
    respuesta = requests.get(url)
    return respuesta.json()["results"]  # Extrae la lista de personajes

def crear_tabla_hash(personajes):
    """
    Crea una tabla hash (diccionario) usando el nombre del personaje como clave
    para búsquedas rápidas.
    """
    return {personaje["name"]: personaje for personaje in personajes}

def buscar_personaje(nombre, tabla_hash):
    """
    Busca un personaje por nombre dentro de la tabla hash.
    """
    return tabla_hash.get(nombre, "Personaje no encontrado")


personajes = obtener_personajes_starwars()
tabla_hash = crear_tabla_hash(personajes)


resultado = buscar_personaje("Darth Vader", tabla_hash)
print(resultado)  