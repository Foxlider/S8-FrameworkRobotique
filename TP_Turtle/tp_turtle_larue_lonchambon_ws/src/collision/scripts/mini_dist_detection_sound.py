#!/usr/bin/env python
# license removed for brevity
import rospy
import numpy as np
import math
from sensor_msgs.msg import LaserScan
from kobuki_msgs.msg import Sound
from std_msgs.msg import Float32

def min_sans_nan(tbl):
    m = ""
    index = 0
    for i in range(len(tbl)):
        if m == "" :
            m = tbl[i]
        elif tbl[i].isdigit():
            if tbl[i] < m:
                m = tbl[i]
                index = i
    
    return m, index


def callback(laserScanMsg):

    ranges = laserScanMsg.ranges
    minvalue = np.nanmin(ranges)

    rospy.loginfo(rospy.get_caller_id() + "\nminvalue %s %s", minvalue, type(minvalue))

    cmd = Sound()
    cmd.value = 3
    pub.publish(cmd)
    if(not np.isnan(minvalue)):
        rospy.sleep(minvalue/5)

    
def listener():
    rospy.init_node('min_dist_detection', anonymous=True)
    rospy.Subscriber("scan", LaserScan, callback, queue_size=1)
    rospy.spin()


if __name__ == '__main__':
    try:
        pub = rospy.Publisher('mobile_base/commands/sound', Sound, queue_size=1)
        rospy.loginfo(rospy.get_caller_id() + " started")
        listener()
    except rospy.ROSInterruptException:
        pass
