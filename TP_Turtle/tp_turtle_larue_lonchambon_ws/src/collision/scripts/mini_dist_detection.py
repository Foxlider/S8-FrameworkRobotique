#!/usr/bin/env python
# license removed for brevity
import rospy
import numpy as np
import math
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32


def callback(laserScanMsg):

    # Get minimal value from all the laser ranges
    ranges = laserScanMsg.ranges
    minvalue = np.nanmin(ranges)

    # log value to term
    rospy.loginfo(rospy.get_caller_id() + "\nminvalue %s", minvalue)

    # publish to /min_dist
    pub.publish(minvalue)

    
def listener():
    rospy.init_node('min_dist_detection', anonymous=True)

    #Subscribe to laser scan topic and only keep the last message
    rospy.Subscriber("scan", LaserScan, callback, queue_size=1)

    # Keepalive
    rospy.spin()

def main(args=None):
    s


if __name__ == '__main__':
    try:
        # Publisher
        pub = rospy.Publisher('min_dist', Float32, queue_size=1)

        #That does NOT log
        rospy.loginfo(rospy.get_caller_id() + " started")
        listener()
    except rospy.ROSInterruptException:
        pass
