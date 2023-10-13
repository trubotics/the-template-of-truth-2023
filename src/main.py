# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       wandows man                                                  #
# 	Created:      10/13/2023, 9:01:10 a.m.                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

# Define the controller
controller1 = Controller(ControllerType.PRIMARY)
# controller2 = Controller(ControllerType.PARTNER)

# Define Motors
# variable = Motor(port number, gear ratio (green=18-1, red=36-1, blue=6-1), reverse)
leftMotor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
rightMotor = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
drivetrain = DriveTrain(leftMotor, rightMotor)

# TODO: Define the claw and arm motors here:

####

def pre_auton():
    brain.screen.print("Hello World!")

def autonomous():
    drivetrain.drive_for(FORWARD, 100, MM)
    # TODO: Make the robot do a dance!

def drivercontrol():
    while True:
        # Tank drive
        leftMotor.spin(FORWARD, controller1.axis3.position(), PERCENT)
        rightMotor.spin(FORWARD, controller1.axis2.position(), PERCENT)

        # Claw control
        # TODO: Add claw control here:
        
        ####

competition = Competition(drivercontrol, autonomous)
