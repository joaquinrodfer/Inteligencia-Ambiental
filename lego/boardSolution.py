#from pybricks.ev3devices import Motor, ColorSensor 
from city_map import CityMap
arrSolucion2 = {(6,4),(6,3),(5,3),(4,3),(4,4)}

mapNotMQTT = "0202000105030705000200041109060110031000000200080101100110000106010701"
miPilaLoQueHase=[]

def calculoSiguienteCasilla(arrSolucion):
    for i in range(len(arrSolucion)):
        casillaSiguiente = arrSolucion[i+1]
        casillaActual = arrSolucion[i]
        casillaAnterior = arrSolucion[i-1]

        if(casillaSiguiente[0] == casillaActual[0]):
            #Hay que seguir recto porque el siguiente movimiento es en la misma fila o columna
            #Orientacion 0=ARRIBA 1=ABAJO 2=IZQUIERDA 3=DERECHA 
            orientacion = 0 if casillaAnterior[0] == casillaActual[0] and casillaAnterior[1] > casillaActual[1] else 1
            if (casillaActual[1] > casillaSiguiente[1]):
                if(orientacion == 2):
                    loquehase=0
                elif orientacion == 0:
                    loquehase=-90
                elif orientacion == 1:
                    loquehase=90
                else:
                    loquehase=-180
            elif (casillaActual[1] < casillaSiguiente[1]):
                if(orientacion == 2):
                    loquehase=180
                elif orientacion == 0:
                    loquehase=90
                elif orientacion == 1:
                    loquehase=-90
                else:
                    loquehase=0
        
        elif(casillaSiguiente[1] == casillaActual[1]):
                #Orientacion 0=ARRIBA 1=ABAJO 2=IZQUIERDA 3=DERECHA 
                orientacion = 2 if casillaAnterior[0] > casillaActual[0] and casillaAnterior[1] == casillaActual[1] else 3
        if(casillaActual[0] > casillaSiguiente[0]):
                if(orientacion == 2):
                        loquehase=-90
                elif orientacion == 0:
                    loquehase=-180
                elif orientacion == 1:
                    loquehase=0
                else:
                    loquehase=90
        elif(casillaActual[0] < casillaSiguiente[0]):
                if(orientacion == 2):
                        loquehase=90
                elif orientacion == 0:
                    loquehase=0
                elif orientacion == 1:
                    loquehase=-180
                else:
                    loquehase=-90
        miPilaLoQueHase.append(loquehase)

cityMap = CityMap(mapNotMQTT)
#print(cityMap.find_quickest_path((6,4),(4,4)))