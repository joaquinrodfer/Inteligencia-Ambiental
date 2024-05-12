#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

left_motor = Motor(Port.D)
right_motor = Motor(Port.A)

line_sensor = ColorSensor(Port.S4)

gyroscopic_sensor = GyroSensor(Port.S1, Direction.COUNTERCLOCKWISE)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

BLACK = 10
WHITE = 85
threshold = (BLACK + WHITE) / 2

DRIVE_SPEED = 120

PROPORTIONAL_GAIN = 2.4

counter = 0

test = [0, 0, -100, 0, 0, 0, 0, 0, 0, 0, -100, 0, 100, 0, 0, 0, 100, 0]

while True:
    gyroscopic_sensor.reset_angle(0)
    robot.turn(90)
    print(gyroscopic_sensor.angle())
    wait(5000)
    gyroscopic_sensor.reset_angle(0)
    robot.turn(-90)
    print(gyroscopic_sensor.angle())
    break


    # deviation = line_sensor.reflection() - threshold

    # if line_sensor.reflection() < 10:
    #     print(test)
    #     if test is not None:
    #         actual = test.pop(0)
    #     else:
    #         robot.stop()
    #         break
    #     if actual == 0:
    #         robot.drive(DRIVE_SPEED, 0)
    #     else:
    #         robot.straight(50)
    #         gyroscopic_sensor.reset_angle(0)
    #         robot.turn(actual)
    #         if test is not None:
    #             test.pop(0)
    #         print(gyroscopic_sensor.angle())
    #         if actual == 100:
    #             robot.turn((gyroscopic_sensor.angle()-80))
    #         else:
    #             robot.turn(-(gyroscopic_sensor.angle()-(-80)))
    #         robot.drive(DRIVE_SPEED, 0)
            
    #         wait(500)
    #     wait(800)    