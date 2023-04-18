#!/usr/bin/env python
# license removed for brevity
import rospy
import numpy as np
from kobuki_msgs.msg import Sound
from std_msgs.msg import Float32


class ProximitySoundFeedback():

    def __init__(self):
        rospy.init_node('sound_min_dist_feedback', anonymous=True)
        self.pub = rospy.Publisher('mobile_base/commands/sound', Sound, queue_size=1)

        self.sub = rospy.Subscriber("min_dist", Float32, self.min_dist_callback, queue_size=1)


    def min_dist_callback(self, minValue):
        rospy.loginfo(rospy.get_caller_id() + "\nminValue %s", minValue)

        cmd = Sound()
        cmd.value = 3
        self.pub.publish(cmd)
        if(not np.isnan(minValue.data)):
            rospy.sleep(minValue.data/5)


def main(args=None):

    soundFeedback = ProximitySoundFeedback()

    rospy.spin()

if __name__ == '__main__':
    main()