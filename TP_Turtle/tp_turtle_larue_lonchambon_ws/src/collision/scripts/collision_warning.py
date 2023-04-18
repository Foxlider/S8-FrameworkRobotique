#!/usr/bin/env python
# license removed for brevity
import rospy
from kobuki_msgs.msg import BumperEvent
from kobuki_msgs.msg import Sound





class BumperSoundFeedback():

    def __init__(self):
        rospy.init_node('collision_warning', anonymous=True)
        self.pub = rospy.Publisher('mobile_base/commands/sound', Sound, queue_size=1)

        self.sub = rospy.Subscriber("/mobile_base/events/bumper", BumperEvent, self.bumper_callback)

    def bumper_callback(self, event):
        rospy.logdebug(rospy.get_caller_id() + "I heard %s", event)


        if(event.state):
            return
        
        rospy.loginfo(rospy.get_caller_id() + "I heard %s on bumper %s", event.state, event.bumper)

        cmd = Sound()
        cmd.value = 4
        self.pub.publish(cmd)
        rospy.sleep(0.2)
        # cmd.value = Sound.ERROR
        # pub.publish(cmd)
        for i in range(event.bumper+1):
            rospy.sleep(0.1)
            cmd = Sound()
            cmd.value = 3
            self.pub.publish(cmd)


def main(args=None):

    soundFeedback = BumperSoundFeedback()

    rospy.spin()

if __name__ == '__main__':
    main()