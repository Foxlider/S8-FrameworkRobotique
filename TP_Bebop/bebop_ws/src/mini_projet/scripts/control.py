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





class DroneControllerSim():
    def __init__(self):
        rospy.init_node('control_sim', anonymous=True)

        # Publishers
        self.pubTakeoff = rospy.Publisher('bebop/takeoff', Empty, queue_size=1)
        self.pubLand = rospy.Publisher('bebop/land', Empty, queue_size=1)
        self.pubReset = rospy.Publisher('bebop/reset', Empty, queue_size=1)
        # pubTricks = rospy.Publisher('bebop/', Empty,queue_size=1)
        self.pub = rospy.Publisher('bebop/cmd_vel', Twist, queue_size=2)

        self.sentry_mode_on = False

        # Services
        # self.sentryMode = rospy.Service("sentry_mode", SentryMode, self.sentry_mode_service)
        # self.sentryMode = rospy.Service("fun_mode", FunMode, self.fun_mode_service)

        # Subscribers
        self.sub = rospy.Subscriber("/bebop2/joy", Joy, self.callback, queue_size=1)


        # self.loop()

    def loop(self):
        while not rospy.is_shutdown():
            self.rate = rospy.Rate(10)
            self.rate.sleep()


    def callback(self, joy):
        """
            The joy/game-pad message callback.

            :type   joy:    Joy
            :param  joy:    The incoming joy message.

        """
        self.axes = joy.axes
        self.buttons = joy.buttons
        rospy.logdebug(rospy.get_caller_id() + "I heard %s", joy.axes)
        rospy.logdebug(rospy.get_caller_id() + "I heard %s", joy.buttons)

        # EMERGENCY RESET
        if(self.buttons[SELECT] and self.buttons[START]):
            reset = Empty()
            rospy.loginfo(rospy.get_caller_id() + "  STOP !!")
            self.pubReset.publish(reset)
            rospy.sleep(1)
            return
        

        # SENTRY MODE SWITCH
        if(self.buttons[R_BUMPER]):
            rospy.loginfo(rospy.get_caller_id() + "  SWITCH MODE")
            self.sentry_mode_on = not self.sentry_mode_on
            return

        # LAND DRONE
        if(self.buttons[SELECT]):
            land = Empty()
            rospy.loginfo(rospy.get_caller_id() + "  LANDING")
            self.pubLand.publish(land)
            return
        
        # START DRONE
        if(self.buttons[START]):
            takeoff = Empty()
            rospy.loginfo(rospy.get_caller_id() + "  TAKING OFF")
            self.pubTakeoff.publish(takeoff)
            return
        
        # FUN COMMANDS
        if(self.buttons[L_BUMPER] and self.buttons[BTN_X]):
            rospy.loginfo(rospy.get_caller_id() + "  FLIP LEFT")
            return
        
        
        # DRONE MOVEMENT
        cmd = Twist()

        # sentry mode switch
        if(self.sentry_mode_on):
            cmd.angular.z = 0.5
        else:
            cmd.linear.x = self.axes[L_STICK_Y]
            cmd.linear.y = self.axes[L_STICK_X]
            cmd.linear.z = - self.axes[TRIGGERS]
            cmd.angular.z = self.axes[R_STICK_X]

        rospy.loginfo(rospy.get_caller_id() + " %f|%f|%f -- %f", cmd.linear.x, cmd.linear.y, cmd.linear.z, cmd.angular.z )
        self.pub.publish(cmd)



def main(args=None):

    controller= DroneControllerSim()

    rospy.spin()

if __name__ == '__main__':
    main()