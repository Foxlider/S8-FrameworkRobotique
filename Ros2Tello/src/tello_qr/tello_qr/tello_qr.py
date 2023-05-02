#!/usr/bin/env python3

import sys
import time
import cv2
import imutils
import numpy as np
import rclpy
from rclpy.node import Node

from std_msgs.msg import Empty
from nav_msgs.msg import Twist


class tello_qr(Node):

    def __init__(self):
        super().__init__('tello_qr')
        self.subscription = self.create_subscription(String, 'barcode', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(Twist, 'control', 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        behaviour = msg.data
        self.get_logger().info('I heard: "%s"' % behaviour)
        match behaviour:
            case "start":
                # Start travelling
                return false
            case "finish":
                # Finish travelling
                return false
            case "stop":
                # Force Stop
                # TODO
                return false        

def main():

    rclpy.init(args=args)

    tello_qr = tello_qr()
    
    rclpy.spin(tello_qr)        

if __name__ == '__main__':
    main()
