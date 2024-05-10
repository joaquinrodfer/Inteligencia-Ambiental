#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Direction, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from math import sqrt

left_motor = Motor(Port.D)
right_motor = Motor(Port.A)

gancho = Motor(Port.B)

line_sensor = ColorSensor(Port.S4)

gyroscopic_sensor = GyroSensor(Port.S1, Direction.COUNTERCLOCKWISE)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=118)
hub = EV3Brick()

BLACK = 10
GREEN = 45

WHITE = 90
threshold = (GREEN + 10) / 2

TURN_SPEED = 65
TURN_ANGLE = 37

DRIVE_SPEED = 75

# De 6,5 a 0,4
# road = [0, 0, -90, 0, 0, 0, 0, 0, 0, 0, -90, 0, 90, 0, 0, 0, 90, 0]
# back = [180, 0, -90, 0, 0, 0, -90, 0, 90, 0, 0, 0, 0, 0, 0, 0, 90]

road = [0, 0, 90, 0,0,0,0,0,0,0,-90,0,0,0,-90,0,0,0,0,0,-90,0]
back = [180,0,90,0,0,0,0,0,90,0,-90,0,90,0,-90]

road2 = [0, 90, 0, -90, 0, -90, 0, 90, 0, -90, 0]
back2 = [180, 0, 90 ,0, -90,0,0,0,-90,0,0,0,0,0, 0, 0, 90]

gancho.run_target(200, 150)
ganchoEstado = 1

estado = 1

last_read = ''

FILTRO_DE = 20

# while True:
#     hub.screen.draw_text(40, 50, line_sensor.reflection())
#     wait(1000)
#     hub.screen.clear()

# while True:
#     if line_sensor.color() == Color.BLUE:
#         robot.drive(TURN_SPEED, 20*estado)
#         estado = 1 if estado == -1 else -1
#     elif line_sensor.color() == Color.GREEN:
#         robot.straight(30)
#     elif line_sensor.color() == Color.BLACK:
#         robot.straight(30)


cont = 0
# while True:
#     if line_sensor.reflection() > 60:
#         robot.drive(TURN_SPEED, 0)
#         cont = 0;
#     else:
#         robot.turn((5+cont*5)*estado)
#         estado = 1 if estado == -1 else -1
#         cont += 1

verde = [30, 70, 30]

def distancia_euclidea(r1, g1, b1, r2, g2, b2):
    return sqrt((r1-r2)**2+(g1-g2)**2+(b1-b2)**2)

# while True:
#     print(line_sensor.rgb())
#     print(distancia_euclidea(26, 50, 24, line_sensor.rgb()[0], line_sensor.rgb()[1], line_sensor.rgb()[2]))
#     print("=====================================")
    
#     wait(1000)
#     hub.screen.clear()


last_read = ''
cont = 0
cont_road = 0

while True:
    if line_sensor.color() == Color.BLACK and last_read != Color.BLACK:
        last_read = Color.BLACK
        if road != []:
            actual = road.pop(0)
        else:
            if back != []:
                road = back
                back = []
                actual = road.pop(0)
            else:
                robot.straight(100)
                robot.stop()
                actual = 180
                gancho.stop()
                if road2 == [] and back2 == []:
                    robot.straight(10)
                    gancho.run_target(200, 150)
                    robot.straght(50)
                    robot.stop()
                    break
        if actual == 0:
            while line_sensor.color() == Color.BLACK:
                robot.drive(DRIVE_SPEED, -10)
        else:
            if actual == 180:
                robot.straight(10)
                if ganchoEstado == 1:
                    gancho.run_target(200, 0)
                    ganchoEstado = 0
                else:
                    gancho.run_target(200, 150)
                    robot.straight(50)
                    ganchoEstado = 1
                    road = road2
                    back = back2
                    road2 = []
                    back2 = []
                
                robot.turn(-165)
                gyroscopic_sensor.reset_angle(0)
                while distancia_euclidea(verde[0], verde[1], verde[2], line_sensor.rgb()[0], line_sensor.rgb()[1], line_sensor.rgb()[2]) > FILTRO_DE:
                    robot.turn(-10)
                robot.turn(-20)
            else:
                robot.straight(30)
                cont = 0
                if actual == 90:
                    robot.drive(TURN_SPEED, 10)
                    while distancia_euclidea(verde[0], verde[1], verde[2], line_sensor.rgb()[0], line_sensor.rgb()[1], line_sensor.rgb()[2]) > FILTRO_DE:
                        cont += 1
                        robot.turn(16*estado)
                        robot.straight(4)
                    robot.drive(TURN_SPEED, -TURN_ANGLE)
                    estado = 1
                else:
                    robot.drive(TURN_SPEED, -10)
                    while distancia_euclidea(verde[0], verde[1], verde[2], line_sensor.rgb()[0], line_sensor.rgb()[1], line_sensor.rgb()[2]) > FILTRO_DE:
                        cont += 1
                        robot.turn(-12*estado)
                        robot.straight(5)
                    robot.turn(-45)
                    estado = 1
                
    elif distancia_euclidea(verde[0], verde[1], verde[2], line_sensor.rgb()[0], line_sensor.rgb()[1], line_sensor.rgb()[2]) < FILTRO_DE:
        robot.drive(DRIVE_SPEED, -TURN_ANGLE)
        last_read = Color.GREEN
    else:
        robot.drive(DRIVE_SPEED, TURN_ANGLE)
        last_read = Color.WHITE