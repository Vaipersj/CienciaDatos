print('#1 Carga de Datos: lista de ventas original.')
#Diccionario de ventas
ventas = [
    {"fecha": "2025-05-12", "producto": "Pizzas", "cantidad": 4, "precio": 6.990},
    {"fecha": "2025-05-13", "producto": "Completos", "cantidad": 5, "precio": 1.500},
    {"fecha": "2025-05-14", "producto": "Papas", "cantidad": 10, "precio": 2.000},
    {"fecha": "2025-05-15", "producto": "Churrascos", "cantidad": 3, "precio": 3.000},
    {"fecha": "2025-05-16", "producto": "HandRoll", "cantidad": 7, "precio": 2.500},
    {"fecha": "2025-05-17", "producto": "Pizzas", "cantidad": 7, "precio": 7.990},
    {"fecha": "2025-05-18", "producto": "Papas", "cantidad": 4, "precio": 2.000},
    {"fecha": "2025-05-19", "producto": "Churrascos", "cantidad": 5, "precio": 2.500},
    {"fecha": "2025-05-20", "producto": "HandRoll", "cantidad": 7, "precio": 2.500}
]
print(ventas)
print(' ')

print('#2 Cálculo de Ingresos Totales: Los ingresos totales generados.')
ingresos_totales = 0 #Crea e inicializa variable

for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]  # Multiplicar cantidad por precio y sumar

print(f"Ingresos totales: ${ingresos_totales:.2f}") #Total de ingresos 
print(' ')

print('#3 Análisis del Producto Más Vendido: El producto más vendido y su cantidad total vendida.')
ventas_por_producto = {} #Crea e incializa Diccionario

for venta in ventas:
    producto = venta["producto"] #Obtiene Producto
    cantidad = venta["cantidad"] #Obtiene Cantidad
    
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad #Si producto existe le suma la nueva cantidad al diccionario
    else:
        ventas_por_producto[producto] = cantidad #Si el producto NO existe lo agrega con su cantidad inicial

# Identificar el producto más vendido
#Se crea funcion que hace el calculo al pasarle el diccionario
def productoTopVentas(ventas_por_producto):
    producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
    print(f"Producto más vendido: {producto_mas_vendido} con {ventas_por_producto[producto_mas_vendido]} unidades vendidas.")

productoTopVentas(ventas_por_producto)
print(' ')

print('#4 Promedio de Precio por Producto: El precio promedio de venta por producto.')
precios_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    total_precio = venta["cantidad"] * venta["precio"]  # Suma total de ventas para ese producto
    cantidad_total = venta["cantidad"]  # Cantidad vendida

    if producto in precios_por_producto:
        precios_por_producto[producto] = (
            precios_por_producto[producto][0] + total_precio,  # Suma de ingresos totales
            precios_por_producto[producto][1] + cantidad_total  # Suma de unidades vendidas
        )
    else:
        precios_por_producto[producto] = (total_precio, cantidad_total)

# Calcular el precio promedio de venta por producto
def precioPromedioXVenta(precios_por_producto):
    precio_promedio_por_producto = {
                    producto: round(total_precio / cantidad_total,2)
                    for producto, (total_precio, cantidad_total) in precios_por_producto.items()
    }

    # Imprimir resultados
    print("Precios por producto:", precios_por_producto)
    print("Precio promedio por producto:", precio_promedio_por_producto)

precioPromedioXVenta(precios_por_producto)
print(' ')

print('#5 Ventas por Día: Los ingresos totales por día.')
# Crear el diccionario ingresos_por_dia
ingresos_por_dia = {}

for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]  # Ingresos Totales
    
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso  # Sumar ingresos a la fecha existente
    else:
        ingresos_por_dia[fecha] = ingreso  # Crear nueva entrada con ingresos

# Imprimir los ingresos por día
for fecha, ingreso in ingresos_por_dia.items():
    print(f"Fecha: {fecha}, Ingreso total: ${ingreso:.2f}")

print(' ')

print('#6 Representación de Datos: El resumen de ventas por producto.')
# Crear el diccionario resumen_ventas
resumen_ventas = {}

for venta in ventas:
    producto = venta["producto"]
    total_ingresos = venta["cantidad"] * venta["precio"]  # Ingresos generados por la venta
    cantidad_total = venta["cantidad"]  # Cantidad vendida

    if producto in resumen_ventas:
        resumen_ventas[producto]["cantidad_total"] += cantidad_total
        resumen_ventas[producto]["ingresos_totales"] += total_ingresos
    else:
        resumen_ventas[producto] = {
            "cantidad_total": cantidad_total,
            "ingresos_totales": total_ingresos
        }

# Calcular precio promedio por producto
for producto, datos in resumen_ventas.items():
    datos["precio_promedio"] = datos["ingresos_totales"] / datos["cantidad_total"]

# Imprimir resultados
for producto, datos in resumen_ventas.items():
    print(f"{producto}: {datos}")
