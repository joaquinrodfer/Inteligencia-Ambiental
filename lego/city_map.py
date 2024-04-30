from road import Road

class CityMap:
    def __init__(self, mapCode) -> None:
        self.cityMap = self.__parse_map(mapCode)

    def distancia_manhattan(self, pos_actual, pos_destino):
        return abs(pos_actual[0] - pos_destino[0]) + abs(pos_actual[1] - pos_destino[1])
    
    def print_directions(self):
        for row in self.cityMap:
            for road in row:
                print(road.directions)
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
