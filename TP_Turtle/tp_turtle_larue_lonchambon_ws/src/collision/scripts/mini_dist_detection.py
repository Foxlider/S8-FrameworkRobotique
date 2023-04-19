#!/usr/bin/env python
# license removed for brevity
import rospy
import numpy as np
import math
from sensor_msgs.msg import LaserScan
from kobuki_msgs.msg import Sound
from std_msgs.msg import Float32

class MinDistDetector:

    def __init__(self):
        self.pub = rospy.Publisher('mobile_base/commands/sound', Sound, queue_size=1)
        rospy.init_node('min_dist_detection', anonymous=True)
        rospy.Subscriber("scan", LaserScan, self.callback, queue_size=1)
        rospy.loginfo(rospy.get_caller_id() + " started")
        rospy.spin()

    def callback(self, laserScanMsg):
        ranges = laserScanMsg.ranges
        minvalue = np.nanmin(ranges)

        rospy.loginfo(rospy.get_caller_id() + "\nminvalue %s %s", minvalue, type(minvalue))

        cmd = Sound()
        cmd.value = 3
        self.pub.publish(cmd)
        if(not np.isnan(minvalue)):
            rospy.sleep(minvalue/5)

def main(args=None):
    try:
        detector = MinDistDetector()
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()

