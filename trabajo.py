# Programa 1: Búsqueda en Arreglo Multidimensional

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):          # Recorre filas
        for j in range(len(matriz[i])):   # Recorre columnas
            if matriz[i][j] == valor:
                return i, j
    return None

# Matriz de ejemplo 3x3
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("Matriz:")
for fila in matriz:
    print(fila)

valor_buscado = int(input("\nIngrese el valor que desea buscar: "))
resultado = buscar_valor(matriz, valor_buscado)

if resultado:
    print(f"✅ Valor {valor_buscado} encontrado en la posición: fila {resultado[0]}, columna {resultado[1]}")
else:
    print(f"❌ El valor {valor_buscado} no se encuentra en la matriz.")
