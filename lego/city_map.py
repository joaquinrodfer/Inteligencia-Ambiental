from road import Road
from collections import deque

class CityMap:
    def __init__(self, mapCode) -> None:
        self.cityMap = self.__parse_map(mapCode)
        self.solutions = []
    
    def print_streets(self):
        for row in self.cityMap:
            for road in row:
                print(road.street, end=" ")
            print()

    def print_map_codes(self):
        for row in self.cityMap:
            for road in row:
                print(road.code, end=" ")
            print()
    
    def __parse_map(self, mapCode):
        pairs = [mapCode[i:i+2] for i in range(0, len(mapCode), 2)]

        matrix = []
        for i in range(7):
            row = pairs[i*5:i*5+5]
            for j in range(5):
                row[j] = Road(row[j], (i, j))

            matrix.append(row)

        return matrix
    
    def __get_matrix(self):
        matrix = []
        array = []
        for row in self.cityMap:
            for road in row:
                array.append(road.street)
            matrix.append(array)
            array = []
        return matrix
    
    def find_quickest_path(self, begin, end):
        return self.__find_quickest_path(self.__get_matrix(), begin, end)

    def __find_quickest_path(self, matrix, begin, end):
        if begin == end:
            return []

        rows = len(matrix)
        cols = len(matrix[0])

        visitado = set()
        padre = {}

        queue = deque()
        queue.append(begin)
        visitado.add(begin)

        while queue:
            actual = queue.popleft()

            if actual == end:
                # Reconstruir el camino más corto
                return self.__build_road(padre, begin, end)

            vecinos = self.__get_neighbors(actual, rows, cols)
            for vecino in vecinos:
                if vecino not in visitado and matrix[vecino[0]][vecino[1]] == 1:
                    visitado.add(vecino)
                    queue.append(vecino)
                    padre[vecino] = actual

        return "No se encontró camino"
    
    def __build_road(self, father, begin, end):
        camino = []
        actual = end
        while actual != begin:
            camino.insert(0, actual)
            actual = father[actual]
        camino.insert(0, begin)
        return camino
    
    def __get_neighbors(self, actual, rows, cols):
        i, j = actual
        vecinos = []
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in movimientos:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols:
                vecinos.append((ni, nj))
        return vecinos
        