import requests

def get_countries():
    """Obtiene datos de países desde la API correcta"""
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error al obtener datos: {response.status_code}")

def sort_countries_by_population(countries):
    """Ordena países por población"""
    return sorted(countries, key=lambda x: x.get('population', 0))

def binary_search_country_by_name(countries, target_name):
    """Busca un país por nombre usando búsqueda binaria"""
    left, right = 0, len(countries) - 1
    
    while left <= right:
        mid = (left + right) // 2
        current_name = countries[mid].get('name', {}).get('common', '').lower()
        
        if current_name == target_name.lower():
            return countries[mid]
        elif current_name < target_name.lower():
            left = mid + 1
        else:
            right = mid - 1
    
    return None

# Uso correcto
if __name__ == "__main__":
    try:
        countries = get_countries()
        sorted_countries = sort_countries_by_population(countries)
        
        # Ejemplo de búsqueda
        target_country = "Ecuador"
        result = binary_search_country_by_name(sorted_countries, target_country)
        
        if result:
            print(f"País encontrado: {result['name']['common']} - Población: {result['population']}")
        else:
            print(f"País '{target_country}' no encontrado")
            
    except Exception as e:
        print(f"Error: {e}")
    
