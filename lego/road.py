class Road:
    def __init__(self, code, coordinates):
        self.code = code
        self.directions = self.__parse_directions(code)
        self.coordinates = coordinates
        self.neighbors = []

    def get_codes(self,fila,columna):
        return self.code

    def __parse_directions(self, code):
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
        