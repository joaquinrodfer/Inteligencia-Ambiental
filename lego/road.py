class Road:
    def __init__(self, code, coordinates):
        self.code = code
        self.directions = self.__parse_directions(code)
        self.coordinates = coordinates

    def __parse_directions(self, code):
        if(code == '00'):
            return 0
        else: 
            return 1
        