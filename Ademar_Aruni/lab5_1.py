import json
def cargar alumnos (ruta_archivo):
with open(ruta_archivo, 'r') as archivo:
return json.load(archivo)
def buscar_alumno (alumnos, nombre):
for alumno in alumnos:
if alumno['nombre'].lower() return alumno
return None
==
nombre.lower():
if __name__
ruta =
")
"__main__":
'alumnos.json'
alumnos = cargar_alumnos (ruta)
nombre buscar = input("Ingrese el nombre del alumno a buscar:
resultado = buscar_alumno(alumnos, nombre buscar)
if resultado:
print(f"Alumno encontrado: {resultado}")
else:
print("Alumno no encontrado.")