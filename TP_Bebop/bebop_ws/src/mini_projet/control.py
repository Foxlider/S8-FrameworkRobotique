#!/usr/bin/env python
# license removed for brevity
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

# Controls for the XBOX One Bluetooth Controller


# JOYSTICK AXES VALUES
AXIS_MIN_VAL = -32767
AXIS_MAX_VAL = 32767


# JOYSTICK AXES INDEXES
L_STICK_X = 0
L_STICK_Y = 1
L_TRIGGER = 2
R_STICK_X = 3
R_STICK_Y = 4
R_TRIGGER = 5
L_CROSS_X = 6
L_CROSS_Y = 7
TRIGGERS  = 8


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



pubLand = None
pubTakeoff = None
pubTricks = None
pub = None
# def talker():
#     pub = rospy.Publisher('chatter', String, queue_size=10)
#     rospy.init_node('talker', anonymous=True)
#     rate = rospy.Rate(10) # 10hz
#     while not rospy.is_shutdown():
#         hello_str = "hello world %s" % rospy.get_time()
#         rospy.loginfo(hello_str)
#         pub.publish(hello_str)
#         rate.sleep()

def callback(joy):
    """
        The joy/game-pad message callback.

        :type   joy:    Joy
        :param  joy:    The incoming joy message.

        """
    axes = joy.axes
    buttons = joy.buttons
    rospy.logdebug(rospy.get_caller_id() + "I heard %s", joy.axes)
    rospy.logdebug(rospy.get_caller_id() + "I heard %s", joy.buttons)

    if(buttons[SELECT] and buttons[START]):
        land = Empty()
        rospy.loginfo(rospy.get_caller_id() + "  STOP !!")
        pubLand.publish(land)
        return
    if(buttons[SELECT]):
        land = Empty()
        rospy.loginfo(rospy.get_caller_id() + "  LANDING")
        pubLand.publish(land)
        return
    if(buttons[START]):
        takeoff = Empty()
        rospy.loginfo(rospy.get_caller_id() + "  TAKING OFF")
        pubTakeoff.publish(takeoff)
        return
    
    if(buttons[L_BUMPER] and buttons[BTN_X]):
        rospy.loginfo(rospy.get_caller_id() + "  FLIP LEFT")
        return
    
    cmd = Twist()

    cmd.linear.x = axes[L_STICK_Y]
    cmd.linear.y = axes[L_STICK_X]
    cmd.linear.z = -axes[TRIGGERS]
    cmd.angular.z = axes[R_STICK_X]
    rospy.loginfo(rospy.get_caller_id() + " %f|%f|%f -- %f", cmd.linear.x, cmd.linear.y, cmd.linear.z, cmd.angular.z )
    pub.publish(cmd)

    
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('control_sim', anonymous=True)

    rospy.Subscriber("/bebop2/joy", Joy, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        pubTakeoff = rospy.Publisher('bebop/takeoff', Empty, queue_size=1)
        pubLand = rospy.Publisher('bebop/land', Empty, queue_size=1)
        pubTricks = rospy.Publisher('bebop/', Empty,queue_size=1)
        pub = rospy.Publisher('bebop/cmd_vel', Twist, queue_size=10)
        
        listener()
    except rospy.ROSInterruptException:
        pass
