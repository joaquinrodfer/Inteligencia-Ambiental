def encontrar_camino(matriz, inicio, destino):
    if inicio == destino:
        return []

    rows = len(matriz)
    cols = len(matriz[0])

    camino = []
    visitado = set()
    padre = {}

    camino.append(inicio)
    visitado.add(inicio)

    while camino:
        actual = camino.pop()

        if actual == destino:
            # Reconstruir el camino encontrado
            return reconstruir_camino(padre, inicio, destino)

        vecinos = obtener_vecinos(actual, rows, cols)
        for vecino in vecinos:
            if vecino not in visitado and matriz[vecino[0]][vecino[1]] == 1:
                visitado.add(vecino)
                camino.append(vecino)
                padre[vecino] = actual

    return "No se encontró camino"


def reconstruir_camino(padre, inicio, destino):
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

inicio = (5, 0)
destino = (5, 3)

camino_mas_rapido = encontrar_camino(matriz, inicio, destino)
print("Camino más rápido:", camino_mas_rapido)
