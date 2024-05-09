class Road:
    def __init__(self, code, coordinates):
        self.code = code
        self.street = self.__parse_street(code)
        self.coordinates = coordinates

    def __parse_street(self, code):
        if(code == '00'):
            return 0
        else: 
            return 1
        