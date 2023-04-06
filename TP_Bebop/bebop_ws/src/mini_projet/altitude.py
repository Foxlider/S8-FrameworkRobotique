#!/usr/bin/env python
# license removed for brevity
import rospy
import nav_msgs.msg
import std_msgs.msg

class AltitudePublisher():
    def __init__(self):
        self.pub = rospy.Publisher('altitude', std_msgs.msg.Float64, queue_size=10)
        rospy.init_node('altitudePublisher', anonymous=True)
        rospy.Subscriber("/bebop/odom", nav_msgs.msg.Odometry, self.callback)
        rospy.spin()

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %f", data.pose.pose.position.z)  
        self.pub.publish(data.pose.pose.position.z)
        
if __name__ == '__main__':
    try:
        altitudePublisher = AltitudePublisher()
    except rospy.ROSInterruptException:
        pass