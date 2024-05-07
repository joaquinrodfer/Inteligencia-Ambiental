
from pybricks.parameters import Port
from pybricks.ev3devices import Motor


# Inicializo los motores
motor_left = Motor(Port.A)
motor_right = Motor(Port.D)

# Variables para la posición actual del robot
pos_x = 6# Fila actual
pos_y = 0  # Columna actual


# Función para actualizar la odometría del robot
def actualizar_odometria(direccion):
    global pos_y, pos_x
    if direccion == 'U':
        pos_x -= 1
    elif direccion == 'D':
        pos_x += 1
    elif direccion == 'L':
        pos_y -= 1
    elif direccion == 'R':
        pos_y += 1

    # Compruebo que la posición no sale del mapa
    pos_y = max(0, min(pos_y, 4))  # 5 columnas, índices de 0 a 4
    pos_x = max(0, min(pos_x, 6))  # 7 filas, índices de 0 a 6

    return (pos_y, pos_x)


# Ejemplo de uso
posicion_actual = actualizar_odometria('D')
print(f"El robot está en la casilla: {posicion_actual}")
