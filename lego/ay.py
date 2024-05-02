from collections import deque

def encontrar_camino_mas_rapido(matriz, inicio, destino):
    if inicio == destino:
        return []

    rows = len(matriz)
    cols = len(matriz[0])

    visitado = set()
    padre = {}

    queue = deque()
    queue.append(inicio)
    visitado.add(inicio)

    while queue:
        actual = queue.popleft()

        if actual == destino:
            # Reconstruir el camino más corto
            return reconstruir_camino_mas_corto(padre, inicio, destino)

        vecinos = obtener_vecinos(actual, rows, cols)
        for vecino in vecinos:
            if vecino not in visitado and matriz[vecino[0]][vecino[1]] == 1:
                visitado.add(vecino)
                queue.append(vecino)
                padre[vecino] = actual

    return "No se encontró camino"


def reconstruir_camino_mas_corto(padre, inicio, destino):
    camino = []
    actual = destino
    while actual != inicio:
        camino.insert(0, actual)
        actual = padre[actual]
    camino.insert(0, inicio)
    return camino


def obtener_vecinos(actual, rows, cols):
    i, j = actual
    vecinos = []
    movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for di, dj in movimientos:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols:
            vecinos.append((ni, nj))
    return vecinos


# Ejemplo de uso:
matriz = [
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1]
]

inicio = (6, 0)
destino = (3, 0)

camino_mas_rapido = encontrar_camino_mas_rapido(matriz, inicio, destino)
print("Camino más rápido:", camino_mas_rapido)
