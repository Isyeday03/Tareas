print("Programa 1: Búsqueda en Arreglo Multidimensional")

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado en la matriz."

# Matriz 3x3 de ejemplo
matriz = [
    [4, 8, 3],
    [7, 5, 9],
    [6, 2, 1]
]

valor_a_buscar = int(input("Ingrese el valor a buscar: "))
resultado = buscar_valor(matriz, valor_a_buscar)
print(resultado)

input("Programa 2: Ordenación de una Fila en la Matriz")

def ordenar_fila(matriz, fila):
    matriz[fila].sort()
    return matriz

# Matriz 3x3 de ejemplo
matriz = [
    [4, 8, 3],
    [7, 5, 9],
    [6, 2, 1]
]

fila_a_ordenar = int(input("Ingrese el índice de la fila a ordenar (0-2): "))
print("Matriz original:")
for fila in matriz:
    print(fila)

matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)

