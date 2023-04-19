#!/usr/bin/env python
# license removed for brevity
import rospy
import numpy as np
from kobuki_msgs.msg import Sound
from kobuki_msgs.msg import Led
from std_msgs.msg import Float32


class ProximitySoundFeedbackSaya():

    def __init__(self):
        rospy.init_node('sound_min_dist_feedback', anonymous=True)
        self.pubSnd = rospy.Publisher('mobile_base/commands/sound', Sound, queue_size=1)
        self.pubLed = rospy.Publisher('mobile_base/commands/led', Led, queue_size=1)

        self.rateint=1

        self.sub = rospy.Subscriber("min_dist", Float32, self.min_dist_callback, queue_size=1)

        self.change_rate()

    def min_dist_callback(self, minValue):
        if(not minValue.data.is_integer):
            val = 0
        else:
            val = float(minValue.data)
        
        self.rateint = 20 - 8*val

        rospy.loginfo(rospy.get_caller_id() + "\nminValue %s - rate %s", minValue, self.rateint)
        # if(val > 1):
        #     self.rateint = 1
        # elif val < 1 and val > 0.75

    def change_rate(self):
        while not rospy.is_shutdown():
            if(self.rateint >= 1):
                self.rate = rospy.Rate(self.rateint)
                self.rate.sleep()
                self.pubSnd.publish(Sound(3))
                self.pubLed.publish(Led(1))
                self.pubLed.publish(Led(0))




def main(args=None):

    soundFeedback = ProximitySoundFeedbackSaya()

    rospy.spin()

if __name__ == '__main__':
    main()