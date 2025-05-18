print('Básico: imprime todos los números enteros del 0 al 100.')
num = 0
while num < 101:
    print(num)
    num += 1

print('Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500')
for x in range(0,501,2):
    print(x)
    
print('Contando Vanilla Ice: imprime los números enteros del 1 al 100.')
print('Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”')
for x in range(1,101):
    if x%10 == 0:
        print('baby')
    elif x%5 == 0:
        print('ice ice')
    else:
        print(x)

print('Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 ')
print('e imprime la suma total. (Sorpresa, será un número gigante).')
suma_total = 0
for x in range(0,500001,2):
    suma_total += x
    if x == 500000:
        print (suma_total)
        
print('Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.')
for x in range(2024,0,-3):
    print (x)
    
print('#Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. ')
print('#Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo.')
print('#Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2,')
print('#el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).')

numIncial = 3
numFinal = 10
multiplo = 2
for x in range(numIncial,numFinal+1):
    if x%multiplo == 0:
        print(x)
    