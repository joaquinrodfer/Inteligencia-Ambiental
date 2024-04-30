from road import Road
from best_path import get_neighbors

class CityMap:
    def __init__(self, mapCode) -> None:
        self.cityMap = self.__parse_map(mapCode)
        get_neighbors(self.cityMap)
    
    def print_directions(self):
        for row in self.cityMap:
            for road in row:
                print(road.directions)
            print()

    def get_directions(self,x,y):
        road_object = self.cityMap[x][y]
        return road_object.directions

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
