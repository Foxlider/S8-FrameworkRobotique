#!/usr/bin/env python
# license removed for brevity
import rospy
from kobuki_msgs.msg import BumperEvent
from kobuki_msgs.msg import Sound


def callback(event):
    """
        The bumper message callback.

        :type   event:    BumperEvent
        :param  event:    The incoming bumper message.
    """
    rospy.logdebug(rospy.get_caller_id() + "I heard %s", event)


    if(event.state):
        return
    
    rospy.loginfo(rospy.get_caller_id() + "I heard %s on bumper %s", event.state, event.bumper)

    cmd = Sound()
    cmd.value = 2
    pub.publish(cmd)
    rospy.sleep(0.2)
    # cmd.value = Sound.ERROR
    # pub.publish(cmd)
    for i in range(event.bumper+1):
        rospy.sleep(0.1)
        cmd = Sound()
        cmd.value = 3
        pub.publish(cmd)
        

def listener():
    rospy.Subscriber("/mobile_base/events/bumper", BumperEvent, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    try:
        # In ROS, nodes are uniquely named. If two nodes with the same
        # name are launched, the previous one is kicked off. The
        # anonymous=True flag means that rospy will choose a unique
        # name for our 'listener' node so that multiple listeners can
        # run simultaneously.
        rospy.init_node('collision_warning', anonymous=True)
        
        pub = rospy.Publisher('mobile_base/commands/sound', Sound, queue_size=5)
        rospy.loginfo(rospy.get_caller_id() + " started")
        listener()
    except rospy.ROSInterruptException:
        pass
