# QUADROTOR TRAJECTORY PLANNING  (7/7 points)

'''
In this exercise we placed several beacons in the world. Your task is to stear
the quadrotor through each of them. The order in which you pass through the
beacons does not matter. Instead of flying manually we provide a simple
interface to specify a series of motion commands.
'''

import quadrotor.command as cmd
from math import sqrt


def plan_mission(mission):

    # this is an example illustrating the different motion commands,
    # replace them with your own commands and activate all beacons
    commands  = [
        # middle column
        cmd.up(1),
        cmd.forward(5),
        
        # right column
        cmd.right(2),
        cmd.backward(5),
        
        # left column
        cmd.left(4),
        cmd.forward(6),
        
        
    ]

    mission.add_commands(commands)
