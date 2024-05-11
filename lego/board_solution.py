#from pybricks.ev3devices import Motor, ColorSensor 
from city_map import CityMap

def calculoSiguienteCasilla(arrSolucion, orientacion):
    miPilaLoQueHase=[]
    loquehase=0
    for i in range(len(arrSolucion)-1):
        casillaSiguiente = arrSolucion[i+1]
        casillaActual = arrSolucion[i]

        if(casillaSiguiente[0] == casillaActual[0]):
            #Hay que seguir recto porque el siguiente movimiento es en la misma fila o columna
            #Orientacion 0=ARRIBA 1=ABAJO 2=IZQUIERDA 3=DERECHA 
            if (casillaActual[1] > casillaSiguiente[1]):
                if(orientacion == 2):
                    loquehase=0
                elif orientacion == 0:
                    loquehase=90
                elif orientacion == 1:
                    loquehase=-90
                else:
                    loquehase=-180
            elif (casillaActual[1] < casillaSiguiente[1]):
                if(orientacion == 2):
                    loquehase=180
                elif orientacion == 0:
                    loquehase=-90
                elif orientacion == 1:
                    loquehase=90
                else:
                    loquehase=0
        
        elif(casillaSiguiente[1] == casillaActual[1]):
            #Orientacion 0=ARRIBA 1=ABAJO 2=IZQUIERDA 3=DERECHA
            if(casillaActual[0] < casillaSiguiente[0]):
                if(orientacion == 2):
                        loquehase=90
                elif orientacion == 0:
                    loquehase=-180
                elif orientacion == 1:
                    loquehase=0
                else:
                    loquehase=-90
            elif(casillaActual[0] > casillaSiguiente[0]):
                if(orientacion == 2):
                        loquehase=-90
                elif orientacion == 0:
                    loquehase=0
                elif orientacion == 1:
                    loquehase=-180
                else:
                    loquehase=90
        miPilaLoQueHase.append(loquehase)
        
        miPilaLoQueHase.append(0)

        #Orientacion 0=ARRIBA 1=ABAJO 2=IZQUIERDA 3=DERECHA
        
        if orientacion == 0:
            if loquehase == -90:
                orientacion=3
            elif loquehase == 90:
                orientacion=2
        elif orientacion == 1:
            if loquehase == -90:
                orientacion=2
            elif loquehase == 90:
                orientacion=3
        elif orientacion == 2:
            if loquehase == -90:
                orientacion=0
            elif loquehase == 90:
                orientacion=1
        elif orientacion == 3:
            if loquehase == -90:
                orientacion=1
            elif loquehase == 90:
                orientacion=0

    return miPilaLoQueHase