from road import Road

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
    
    def __get_neighbors(actual, rows, cols):
    i, j = actual
    vecinos = []
    movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for di, dj in movimientos:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols:
            vecinos.append((ni, nj))
    return vecinos
        