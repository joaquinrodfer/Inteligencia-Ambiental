#from pybricks.ev3devices import Motor, ColorSensor 
from city_map import CityMap
arrSolucion2 = {(6,4),(6,3),(5,3),(4,3),(4,4)}

mapNotMQTT = "0202000105030705000200041109060110031000000200080101100110000106010701"
miPilaLoQueHase=[]

def calculoSiguienteCasilla(arrSolucion):
    loquehase=0
    for i in range(len(arrSolucion)-1):
        casillaSiguiente = arrSolucion[i+1]
        casillaActual = arrSolucion[i]
        if i>0:
            casillaAnterior = arrSolucion[i-1]
        else:
            #Aqui se deberia coger el id de la casilla y asi se sabria para donde ir, ya que estamos en una esquina.
            orientacion=2 #Que va hacia la izquierda mirando el mapa desde abajo

        if(casillaSiguiente[0] == casillaActual[0]):
            #Hay que seguir recto porque el siguiente movimiento es en la misma fila o columna
            #Orientacion 0=ARRIBA 1=ABAJO 2=IZQUIERDA 3=DERECHA 
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
            if(casillaActual[0] < casillaSiguiente[0]):
                if(orientacion == 2):
                        loquehase=-90
                elif orientacion == 0:
                    loquehase=-180
                elif orientacion == 1:
                    loquehase=0
                else:
                    loquehase=90
            elif(casillaActual[0] > casillaSiguiente[0]):
                if(orientacion == 2):
                        loquehase=90
                elif orientacion == 0:
                    loquehase=0
                elif orientacion == 1:
                    loquehase=-180
                else:
                    loquehase=-90
        miPilaLoQueHase.append(loquehase)
        
        if loquehase != 0:
            miPilaLoQueHase.append(0)

        #Orientacion 0=ARRIBA 1=ABAJO 2=IZQUIERDA 3=DERECHA
        
        if orientacion == 0:
            if loquehase == 90:
                orientacion=3
            elif loquehase == -90:
                orientacion=2
        elif orientacion == 1:
            if loquehase == 90:
                orientacion=2
            elif loquehase == -90:
                orientacion=3
        elif orientacion == 2:
            if loquehase == 90:
                orientacion=0
            elif loquehase == -90:
                orientacion=1
        elif orientacion == 3:
            if loquehase == 90:
                orientacion=1
            elif loquehase == -90:
                orientacion=0
                
cityMap = CityMap(mapNotMQTT)

print(cityMap.find_quickest_path((6,4),(6,0)))
calculoSiguienteCasilla(cityMap.find_quickest_path((6,4),(6,0)))

print(miPilaLoQueHase)