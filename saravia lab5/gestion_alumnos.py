import json
#Edson saravia
def cargar_alumnos(ruta_archivo):
    # Abre el archivo JSON y carga el contenido
    with open(ruta_archivo, 'r') as archivo:
        return json.load(archivo)

def buscar_alumno(alumnos, nombre):
    # Busca el alumno por nombre
    for alumno in alumnos:
        if alumno['nombre'].lower() == nombre.lower():
            return alumno
    return None

if __name__ == "_main_":
    ruta = 'lab5/alumnos.json'  # Asegúrate de usar la ruta correcta
    alumnos = cargar_alumnos(ruta)
    nombre_buscar = input("Ingrese el nombre del alumno a buscar: ")
    resultado = buscar_alumno(alumnos, nombre_buscar)
    
    if resultado:
        print(f"Alumno encontrado: {resultado}")
    else:
        print("Alumno no encontrado.")
