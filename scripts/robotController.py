#!/usr/bin/env pythonS
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist


class RobotController:

    def __init__(self):
        self.cmd_vel_pub = rospy.Publisher('cmd_vel_mux/input/teleop', Twist, queue_size=1)
        self.twist = Twist()
        self._velocity = 0
        self._angular = 0

    def set_velocity(self, velocity):
        self._velocity = velocity

    def set_angular(self, angular):
        self._angular = angular

    def drive(self):
        self.twist.linear.x = self._velocity
        self.twist.angular.z = self._angular
        self.cmd_vel_pub.publish(self.twist)


if __name__ == "__main__":
    rospy.init_node('robot_drive_controller')
    robotDriveController = RobotController()
    robotDriveController.set_velocity(1)
    robotDriveController.drive()
    rospy.spin()