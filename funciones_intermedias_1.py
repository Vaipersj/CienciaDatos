print('#1. Actualizar valores en diccionarios y listas')
#1 Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
matriz = [ [10, 15, 20], [3, 7, 14] ]
matriz[1][0] = 6
print (matriz)
print (' ')

print('Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”')
print (' ')
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes [0]["nombre"] = "Enrique Martin Morales"
print(cantantes)
print (' ')

print('En ciudades, cambia “Cancún” por “Monterrey”')
print (' ')
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2] = "Monterrey"
print(ciudades)
print (' ')

print('En las coordenadas, cambia el valor de “latitud” por 9.9355431')
print (' ')
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)
print (' ')

print('#2. Iterar a través de una lista de diccionarios')
#Crea la función iterarDiccionario(lista) que reciba 
# una lista de diccionarios y recorra cada diccionario 
# de la lista e imprima cada llave y el valor correspondiente
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario(lista):
    for diccionario in lista:
        print(", ".join([f"{clave} - {valor}" for clave, valor in diccionario.items()]))

iterarDiccionario(cantantes)
print (' ')

print('#3. Obtener valores de una lista de diccionarios')
#Crea la función iterarDiccionario2(llave, lista) que reciba una cadena 
# con el nombre de una llave y una lista de diccionarios. La función debe 
# imprimir el valor almacenado para esa clave de cada diccionario que se 
# encuentra en la lista.
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:  # Verifica si la clave existe en el diccionario
            print(diccionario[llave])
            
iterarDiccionario2("nombre",cantantes)
iterarDiccionario2("pais",cantantes)
print (' ')

print('#4. Iterar a través de un diccionario con valores de lista')
#Crea una función imprimirInformacion(diccionario) que reciba 
# un diccionario en donde los valores son listas. La función 
# debe imprimir el nombre de cada clave junto con el tamaño de 
# su lista y seguido de esto los valores de la lista para esa clave.
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    for clave, valores in diccionario.items():
        print(f"{clave.upper()} {len(valores)} ")
        for valor in valores:
            print(valor)
        print() 
        

imprimirInformacion(costa_rica)
print (' ')