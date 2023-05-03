#!/usr/bin/env python
import time
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy
from std_msgs.msg import Empty
from std_msgs.msg import String
from geometry_msgs.msg import Twist

# SPEEDS
MANUAL_SPEED = 50


# JOYSTICK AXES INDEXES
L_STICK_X = 0
L_STICK_Y = 1
L_TRIGGER = 2
R_STICK_X = 3
R_STICK_Y = 4
R_TRIGGER = 5
L_CROSS_X = 6
L_CROSS_Y = 7


# JOYSTICK BUTTONS INDEXES
L_STICK_PRESS = 9
R_STICK_PRESS = 10
L_BUMPER = 4
R_BUMPER = 5
SELECT = 6
START = 7
XBOX = 8
BTN_A = 0
BTN_B = 1
BTN_X = 2
BTN_Y = 3


class DroneController(Node):
    def __init__(self):
        super().__init__('trello_joy')

        self.get_logger().info("INNIT")

        # Publishers
        self.pubTakeoff = self.create_publisher(Empty, 'takeoff', 1)
        self.pubLand = self.create_publisher(Empty, 'land', 1)
        self.pubReset = self.create_publisher(Empty, 'emergency', 1)
        self.pubTricks = self.create_publisher(String, 'flip', 1)
        self.pub = self.create_publisher(Twist, 'control', 1)

        self.speeds = MANUAL_SPEED
        self.sentry_mode_on = False

        # Services
        # self.sentryMode = rospy.Service("sentry_mode", SentryMode, self.sentry_mode_service)
        # self.sentryMode = rospy.Service("fun_mode", FunMode, self.fun_mode_service)

        # Subscribers
        self.sub = self.create_subscription(Joy, 'joy', self.callback, 1)
        self.get_logger().info("INIT DONE")


        # self.loop()


    def callback(self, joy):
        """
            The joy/game-pad message callback.

            :type   joy:    Joy
            :param  joy:    The incoming joy message.

        """
        self.axes = joy.axes
        self.buttons = joy.buttons
        self.get_logger().debug(f"I heard {joy.axes}")
        self.get_logger().debug(f"I heard {joy.buttons}")

        # EMERGENCY RESET
        if(self.buttons[SELECT] and self.buttons[START]):
            reset = Empty()
            self.get_logger().info("  STOP !!")
            self.pubReset.publish(reset)
            time.sleep(1)
            # rospy.sleep(1)
            return
        

        # SENTRY MODE SWITCH
        if(self.buttons[R_BUMPER]):
            self.get_logger().info("  SWITCH MODE")
            self.sentry_mode_on = not self.sentry_mode_on
            return

        # LAND DRONE
        if(self.buttons[SELECT]):
            land = Empty()
            self.get_logger().info("  LANDING")
            self.pubLand.publish(land)
            time.sleep(1)
            return
        
        # START DRONE
        if(self.buttons[START]):
            takeoff = Empty()
            self.get_logger().info("  TAKING OFF")
            self.pubTakeoff.publish(takeoff)
            time.sleep(1)
            return
        
        # FUN COMMANDS
        if(self.buttons[L_BUMPER] and self.buttons[BTN_X]):
            msg = String()
            msg.data = 'l'
            self.get_logger().info("  FLIP !")
            self.pubTricks.publish(msg)
            time.sleep(4)
            return
        if(self.buttons[L_BUMPER] and self.buttons[BTN_Y]):
            msg = String()
            msg.data = 'f'
            self.get_logger().info("  FLIP !")
            self.pubTricks.publish(msg)
            time.sleep(4)
            return
        if(self.buttons[L_BUMPER] and self.buttons[BTN_B]):
            msg = String()
            msg.data = 'r'
            self.get_logger().info("  FLIP !")
            self.pubTricks.publish(msg)
            time.sleep(4)
            return
        if(self.buttons[L_BUMPER] and self.buttons[BTN_A]):
            msg = String()
            msg.data = 'b'
            self.get_logger().info("  FLIP !")
            self.pubTricks.publish(msg)
            time.sleep(4)
            return
        
        if(self.axes[L_CROSS_Y] != 0):
            self.speeds += self.axes[L_CROSS_Y] * 10
            self.get_logger().info(f"  {self.speeds}")
            time.sleep(0.1)
            return
        
        
        # DRONE MOVEMENT
        cmd = Twist()

        # sentry mode switch
        if(self.sentry_mode_on):
            cmd.angular.z = 0.5
        else:
            cmd.linear.x = - self.axes[L_STICK_X] * self.speeds
            cmd.linear.y = self.axes[L_STICK_Y]  * self.speeds
            cmd.linear.z = ((self.axes[L_TRIGGER] - self.axes[R_TRIGGER])/2 ) * MANUAL_SPEED
            cmd.angular.z = - self.axes[R_STICK_X] * self.speeds

        self.get_logger().info(f" {cmd.linear.x}|{cmd.linear.y}|{cmd.linear.z} -- {cmd.angular.z}")
        self.pub.publish(cmd)




def main(args=None):
    rclpy.init(args=args)

    dronejoy = DroneController()

    rclpy.spin(dronejoy)

    dronejoy.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
