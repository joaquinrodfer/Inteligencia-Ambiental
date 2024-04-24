import time
import os
from queue import PriorityQueue

def distancia_manhattan(pos_actual, pos_destino):
    return abs(pos_actual[0] - pos_destino[0]) + abs(pos_actual[1] - pos_destino[1])

def a_estrella(mapa, inicio, destino):
    cola_abierta = PriorityQueue()
    cola_abierta.put((0, inicio))
    padres = {}
    costos = {inicio: 0}

    while not cola_abierta.empty():
        _, actual = cola_abierta.get()

        if actual == destino:
            # Construir y devolver la ruta
            ruta = []
            while actual in padres:
                ruta.insert(0, actual)
                actual = padres[actual]
            ruta.insert(0, inicio)
            return ruta

        for vecino in obtener_vecinos(mapa, actual):
            nuevo_costo = costos[actual] + 1  # Costo uniforme
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                prioridad = nuevo_costo + distancia_manhattan(vecino, destino)
                cola_abierta.put((prioridad, vecino))
                padres[vecino] = actual

    return None  # No se encontró ruta

def obtener_vecinos(mapa, posicion):
    vecinos = []
    movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Movimientos arriba, abajo, izquierda, derecha
    for dx, dy in movimientos:
        nueva_pos = (posicion[0] + dx, posicion[1] + dy)
        if 0 <= nueva_pos[0] < len(mapa) and 0 <= nueva_pos[1] < len(mapa[0]) and mapa[nueva_pos[0]][nueva_pos[1]] != "00":
            vecinos.append(nueva_pos)
    return vecinos