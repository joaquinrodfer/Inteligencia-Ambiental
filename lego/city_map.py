from road import Road
from best_path import *
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
    
    def parse_directions(self, code):
        if(code == '00'):
            return []
        elif(code == '01'):
            return ['L', 'R']
        elif(code == '02'):
            return ['U', 'D']
        elif(code == '03'):
            return ['U', 'R']
        elif(code == '04'):
            return ['D', 'R']
        elif(code == '05'):
            return ['L', 'D']
        elif(code == '06'):
            return ['L', 'U']
        elif(code == '07'):
            return ['L', 'U', 'R']
        elif(code == '08'):
            return ['U', 'D', 'R']
        elif(code == '09'):
            return ['L', 'D', 'R']
        elif(code == '10'):
            return ['L', 'U', 'D']
        elif(code == '11'):
            return ['L', 'U', 'D', 'R']
        return []
    

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
                
                direccionesCasilla = self.parse_directions(self.cityMap[i][j].code)
                direccionesCasillaAMirar = self.parse_directions(self.cityMap[i+di][j+dj].code)
                
                codeCasilla = self.cityMap[i][j].code
                if (di == -1 and 'U' in direccionesCasilla) or (di == 1 and 'D' in direccionesCasilla) or (dj == -1 and 'L' in direccionesCasilla) or (dj == 1 and 'R' in direccionesCasilla):
                    if (di == -1 and 'D' in direccionesCasillaAMirar) or (di == 1 and 'U' in direccionesCasillaAMirar) or (dj == -1 and 'R' in direccionesCasillaAMirar) or (dj == 1 and 'L' in direccionesCasillaAMirar):
                        vecinos.append((ni, nj))
        return vecinos