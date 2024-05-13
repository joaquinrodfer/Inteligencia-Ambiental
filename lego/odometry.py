
from pybricks.parameters import Port
from pybricks.ev3devices import Motor


# Inicializo los motores
motor_left = Motor(Port.A)
motor_right = Motor(Port.D)

# Variables para la posición actual del robot
pos_x = 6# Fila actual
pos_y = 0  # Columna actual
orientacion=3
direccion=0

# Función para actualizar la odometría del robot

#Orientacion 0=ARRIBA 1=ABAJO 2=IZQUIERDA 3=DERECHA
def actualizar_odometria(direccion, orientacion):
    global pos_y, pos_x
    
    if orientacion == 0: #MIRA HACIA ARRIBA
        if direccion == -90: #derecha
            orientacion=3
            pos_y += 1
        elif direccion == 90: #izquierda
            orientacion=2
            pos_y -= 1
        elif direccion == 180: #mediavuelta
            orientacion=1
            pos_x += 1
    elif orientacion == 1: #MIRA HACIA ABAJO
        if direccion == -90: # izquierda 
            orientacion=2
            pos_y += 1
        elif direccion == 90: # derecha 
            orientacion=3
            pos_y -= 1
        elif direccion == 180: #mediavuelta
            orientacion=0
            pos_x -= 1
    elif orientacion == 2: #MIRA HACIA IZQUIERDA
        if direccion == -90: #arriba
            orientacion=0
            pos_x -= 1
        elif direccion == 90: #abajo
            orientacion=1
            pos_x +=1
        elif direccion == 180: #mediavuelta
            orientacion=3
            pos_y += 1
    elif orientacion == 3: #MIRA HACIA DERECHA
        if direccion == -90: #abajo
            orientacion=1
            pos_x += 1
        elif direccion == 90: #arriba
            orientacion=0
            pos_x -= 1
        elif direccion == 180: #mediavuelta
            orientacion=2
            pos_y -= 1

    pos_y = max(0, min(pos_y, 4))  # 5 columnas, índices de 0 a 4
    pos_x = max(0, min(pos_x, 6))  # 7 filas, índices de 0 a 6
    return (pos_x, pos_y, orientacion)

