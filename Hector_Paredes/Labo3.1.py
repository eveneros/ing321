import requests

def get_countries():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    return response.json()

def quicksort_countries_by_population(countries):
    if len(countries) <= 1:
        return countries
    
    pivot = countries[len(countries) // 2]
    left = [x for x in countries if x.get("population", 0) < pivot.get("population", 0)]
    middle = [x for x in countries if x.get("population", 0) == pivot.get("population", 0)]
    right = [x for x in countries if x.get("population", 0) > pivot.get("population", 0)]
    
    return quicksort_countries_by_population(left) + middle + quicksort_countries_by_population(right)

# Uso:
countries = get_countries()
sorted_countries = quicksort_countries_by_population(countries)

# Ejemplo: imprimir los 10 países menos poblados
for country in sorted_countries[:10]:
    print(f"{country.get('name', {}).get('common', 'Desconocido')}: {country.get('population', 'N/A')}")