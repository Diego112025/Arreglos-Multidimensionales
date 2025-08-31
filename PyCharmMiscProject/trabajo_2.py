# Programa 2: Ordenación de Arreglo Multidimensional

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

# Matriz de ejemplo 3x3
matriz = [
    [34, 12, 25],
    [9, 50, 41],
    [27, 18, 6]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

# Selección de fila
fila_a_ordenar = int(input("\nIngrese el número de la fila a ordenar (0, 1 o 2): "))

if 0 <= fila_a_ordenar < len(matriz):
    bubble_sort(matriz[fila_a_ordenar])
    print("\nMatriz con la fila ordenada:")
    for fila in matriz:
        print(fila)
else:
    print("Número de fila inválido.")

