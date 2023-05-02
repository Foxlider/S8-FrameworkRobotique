# TP 1 : 

## ROS 1

`docker exec -it ros1 /bin/bash`

`printenv | grep ROS`
```sh
root@76c09e0d2db0:~/projects# printenv | grep ROS
ROS_ETC_DIR=/opt/ros/melodic/etc/ros
ROS_ROOT=/opt/ros/melodic/share/ros
ROS_MASTER_URI=http://localhost:11311
ROS_VERSION=1
ROS_PYTHON_VERSION=2
ROS_PACKAGE_PATH=/opt/ros/melodic/share
ROSLISP_PACKAGE_DIRECTORIES=
ROS_DISTRO=melodic

root@76c09e0d2db0:~/projects# mkdir -p ./catkin_ws/src
root@76c09e0d2db0:~/projects# cd catkin_ws/
root@76c09e0d2db0:~/projects/catkin_ws# catkin_make
root@61ff6befac41:~/projects/catkin_ws# source devel/setup.bash 
root@61ff6befac41:~/projects/catkin_ws# echo $ROS_PACKAGE_PATH
/root/projects/catkin_ws/src:/opt/ros/melodic/share
```

### ROS commands

```bash
root@61ff6befac41:~/projects/catkin_ws# rospack find roscpp
/opt/ros/melodic/share/roscpp

root@61ff6befac41:~/projects/catkin_ws# roscd roscpp
root@61ff6befac41:/opt/ros/melodic/share/roscpp# pwd
/opt/ros/melodic/share/roscpp
root@61ff6befac41:/opt/ros/melodic/share/roscpp# roscd roscpp/cmake
root@61ff6befac41:/opt/ros/melodic/share/roscpp/cmake# pwd
/opt/ros/melodic/share/roscpp/cmake

root@61ff6befac41:/opt/ros/melodic/share/roscpp/cmake# rosls roscpp
cmake  msg  package.xml  rosbuild  srv
root@61ff6befac41:/opt/ros/melodic/share/roscpp/cmake# rosls roscpp/cmake
roscpp-msg-extras.cmake  roscpp-msg-paths.cmake  roscppConfig-version.cmake  roscppConfig.cmake
```

```bash
root@61ff6befac41:/opt/ros/melodic/share/roscpp/cmake# roscd ros
ros/                    rosbag/                 rosbuild/               roscpp_core/            rosgraph_msgs/          roslz4/                 rosout/                 rostest/
ros_base/               rosbag_migration_rule/  rosclean/               roscpp_serialization/   roslang/                rosmake/                rospack/                rostime/
ros_comm/               rosbag_storage/         rosconsole/             roscpp_traits/          roslaunch/              rosmaster/              rosparam/               rostopic/
ros_core/               rosbash/                rosconsole_bridge/      roscreate/              roslib/                 rosmsg/                 rospy/                  rosunit/
ros_environment/        rosboost_cfg/           roscpp/                 rosgraph/               roslisp/                rosnode/                rosservice/             roswtf/
```

```bash
root@61ff6befac41:/opt/ros/melodic/share/roscpp/cmake# rosls
actionlib/              diagnostic_msgs/        message_generation/     ros_core/               roscpp/                 roslz4/                 rostime/                topic_tools/
actionlib_msgs/         dynamic_reconfigure/    message_runtime/        ros_environment/        roscpp_core/            rosmake/                rostopic/               trajectory_msgs/
bond/                   gencpp/                 mk/                     rosbag/                 roscpp_serialization/   rosmaster/              rosunit/                visualization_msgs/        
bond_core/              geneus/                 nav_msgs/               rosbag_migration_rule/  roscpp_traits/          rosmsg/                 roswtf/                 xmlrpcpp/
bondcpp/                genlisp/                nodelet/                rosbag_storage/         roscreate/              rosnode/                sensor_msgs/
bondpy/                 genmsg/                 nodelet_core/           rosbash/                rosgraph/               rosout/                 shape_msgs/
catkin/                 gennodejs/              nodelet_topic_tools/    rosboost_cfg/           rosgraph_msgs/          rospack/                smclib/
class_loader/           genpy/                  pluginlib/              rosbuild/               roslang/                rosparam/               std_msgs/
cmake_modules/          geometry_msgs/          ros/                    rosclean/               roslaunch/              rospy/                  std_srvs/
common_msgs/            log/                    ros_base/               rosconsole/             roslib/                 rosservice/             stereo_msgs/
cpp_common/             message_filters/        ros_comm/               rosconsole_bridge/      roslisp/                rostest/                test_results/
```


### Package making

```sh
root@61ff6befac41:~/projects/catkin_ws# cd src/
root@61ff6befac41:~/projects/catkin_ws/src# catkin_create_pkg beginner_tutorial std_msgs rospy roscpp
Created file beginner_tutorial/package.xml
Created file beginner_tutorial/CMakeLists.txt
Created folder beginner_tutorial/include/beginner_tutorial
Created folder beginner_tutorial/src
Successfully created files in /root/projects/catkin_ws/src/beginner_tutorial. Please adjust the values in package.xml.
```

```bash
root@61ff6befac41:~/projects/catkin_ws/src# cd ..
root@61ff6befac41:~/projects/catkin_ws# catkin_make
Base path: /root/projects/catkin_ws
Source space: /root/projects/catkin_ws/src
Build space: /root/projects/catkin_ws/build
Devel space: /root/projects/catkin_ws/devel
Install space: /root/projects/catkin_ws/install
root@61ff6befac41:~/projects/catkin_ws# source devel/setup.bash 
root@61ff6befac41:~/projects/catkin_ws# 
```

```bash
root@61ff6befac41:~/projects/catkin_ws# rosdep update
root@61ff6befac41:~/projects/catkin_ws# rospack depends1 beginner_tutorial 
roscpp
rospy
std_msgs

root@61ff6befac41:~/projects/catkin_ws/src/beginner_tutorial# rospack depends1 rospy
genpy
roscpp
rosgraph
rosgraph_msgs
roslib
std_msgs
```

### ROSCORE and NODES

```bash
triton_09@triton-09:~/catkin_ws$ roscore
... logging to /home/triton_09/.ros/log/b949d0dc-d2ba-11ed-9daa-f8ac65fd6579/roslaunch-triton-09-7316.log
Checking log directory for disk usage. This may take a while.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

started roslaunch server http://triton-09:45503/
ros_comm version 1.14.13


SUMMARY
========

PARAMETERS
 * /rosdistro: melodic
 * /rosversion: 1.14.13

NODES

auto-starting new master
process[master]: started with pid [7330]
ROS_MASTER_URI=http://triton-09:11311/

setting /run_id to b949d0dc-d2ba-11ed-9daa-f8ac65fd6579
process[rosout-1]: started with pid [7341]
started core service [/rosout]
```

```bash
triton_09@triton-09:~/catkin_ws$ rosrun turtlesim turtlesim_node __name:=my_turtle
[ INFO] [1680593916.517835712]: Starting turtlesim with node name /my_turtle
[ INFO] [1680593916.520005366]: Spawning turtle [turtle1] at x=[5,544445], y=[5,544445], theta=[0,000000]
```

```bash
triton_09@triton-09:~/catkin_ws$ rosnode list
/rosout
/turtlesim
triton_09@triton-09:~/catkin_ws$ rosnode list
/my_turtle
/rosout
/turtlesim
triton_09@triton-09:~/catkin_ws$ rosnode ping my_turtle
rosnode: node is [/my_turtle]
pinging /my_turtle with a timeout of 3.0s
xmlrpc reply from http://triton-09:44885/	time=0.684023ms
xmlrpc reply from http://triton-09:44885/	time=1.075983ms
xmlrpc reply from http://triton-09:44885/	time=1.067877ms
xmlrpc reply from http://triton-09:44885/	time=1.075029ms
xmlrpc reply from http://triton-09:44885/	time=1.083851ms
xmlrpc reply from http://triton-09:44885/	time=1.085997ms
xmlrpc reply from http://triton-09:44885/	time=1.077175ms
xmlrpc reply from http://triton-09:44885/	time=1.118183ms
^Cping average: 1.033515ms
```


```bash
rosrun turtlesim turtle_teleop_key
rosrun turtlesim turtlesim_node
```
Ros QT Graph  
![](./doc/rosgraph.png)


```sh
triton_09@triton-09:~/catkin_ws$ rostopic echo /turtle1/cmd_vel 
---
linear: 
  x: 2.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 0.0
---
linear: 
  x: 0.0
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: 2.0
---
```

```sh
triton_09@triton-09:~/catkin_ws$ rostopic list -v

Published topics:
 * /turtle1/color_sensor [turtlesim/Color] 2 publishers
 * /turtle1/cmd_vel [geometry_msgs/Twist] 1 publisher
 * /rosout [rosgraph_msgs/Log] 3 publishers
 * /rosout_agg [rosgraph_msgs/Log] 1 publisher
 * /turtle1/pose [turtlesim/Pose] 2 publishers

Subscribed topics:
 * /turtle1/cmd_vel [geometry_msgs/Twist] 2 subscribers
 * /rosout [rosgraph_msgs/Log] 1 subscriber
 ```

 ```sh
 triton_09@triton-09:~/catkin_ws$ rostopic type /turtle1/cmd_vel 
geometry_msgs/Twist
triton_09@triton-09:~/catkin_ws$ rosmsg show geometry_msgs/Twist
geometry_msgs/Vector3 linear
  float64 x
  float64 y
  float64 z
geometry_msgs/Vector3 angular
  float64 x
  float64 y
  float64 z

triton_09@triton-09:~/catkin_ws$ rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'
publishing and latching message for 3.0 seconds
triton_09@triton-09:~/catkin_ws$ 
```
`rostopic pub` : publish msg  
`-1` : publish 1 message and exit
`/turtle1/cmd_vel` : topic to publish to
`geometry_msgs/Twist` : type of message to send
`--` none of the following args are is an option (avoid treating negative numbers as arguments)


```sh
triton_09@triton-09:~/catkin_ws$ rostopic pub /turtle1/cmd_vel geometry_msgs/Twist -r 10 -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, -1.8]'
^C
triton_09@triton-09:~/catkin_ws$ rostopic pub /turtle1/cmd_vel geometry_msgs/Twist -r 10  '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'
```

```sh
triton_09@triton-09:~/catkin_ws$ rostopic hz /turtle1/pose
subscribed to [/turtle1/pose]
average rate: 62.530
        min: 0.015s max: 0.017s std dev: 0.00051s window: 60
average rate: 62.487
        min: 0.015s max: 0.017s std dev: 0.00050s window: 123
average rate: 62.507
        min: 0.015s max: 0.017s std dev: 0.00051s window: 185
average rate: 62.506
        min: 0.015s max: 0.017s std dev: 0.00050s window: 248
average rate: 62.495
        min: 0.015s max: 0.017s std dev: 0.00050s window: 310
average rate: 62.503
        min: 0.015s max: 0.017s std dev: 0.00050s window: 373
average rate: 62.499
        min: 0.015s max: 0.017s std dev: 0.00050s window: 436
average rate: 62.501
        min: 0.015s max: 0.017s std dev: 0.00049s window: 498
^Caverage rate: 62.502
        min: 0.015s max: 0.017s std dev: 0.00049s window: 539
```

### ROS Service

#### rosservice
```sh
triton_09@triton-09:~/catkin_ws$ rosservice list
/clear
/kill
/my_turtle/get_loggers
/my_turtle/set_logger_level
/reset
/rosout/get_loggers
/rosout/set_logger_level
/rostopic_15141_1680598999710/get_loggers
/rostopic_15141_1680598999710/set_logger_level
/spawn
/teleop_turtle/get_loggers
/teleop_turtle/set_logger_level
/turtle1/set_pen
/turtle1/teleport_absolute
/turtle1/teleport_relative
/turtlesim/get_loggers
/turtlesim/set_logger_level

triton_09@triton-09:~/catkin_ws$ rosservice type /clear
std_srvs/Empty
```

#### ROSPARAM

```sh
triton_09@triton-09:~/catkin_ws$ rosparam list
/my_turtle/background_b
/my_turtle/background_g
/my_turtle/background_r
/rosdistro
/roslaunch/uris/host_triton_09__45503
/rosversion
/run_id
/turtlesim/background_b
/turtlesim/background_g
/turtlesim/background_r
triton_09@triton-09:~/catkin_ws$ rosparam set /turtlesim/background_r 150
triton_09@triton-09:~/catkin_ws$ rosservice call /clear
# It's now clear
```

```sh
triton_09@triton-09:~/catkin_ws$ rosparam get /turtlesim/background_g
86
triton_09@triton-09:~/catkin_ws$ rosparam get /
my_turtle: {background_b: 255, background_g: 86, background_r: 69}
rosdistro: 'melodic

  '
roslaunch:
  uris: {host_triton_09__45503: 'http://triton-09:45503/'}
rosversion: '1.14.13

  '
run_id: b949d0dc-d2ba-11ed-9daa-f8ac65fd6579
turtlesim: {background_b: 255, background_g: 86, background_r: 150}

triton_09@triton-09:~/catkin_ws$ 
```

### RQT Console

```sh
triton_09@triton-09:~/catkin_ws$ rosrun rqt_console rqt_console&
[1] 16420
triton_09@triton-09:~/catkin_ws$ rosrun rqt_logger_level rqt_logger_level&
[2] 16500
```

### ROSED

Basiquement, osef. Ca ouvre `code` ou `vim`.  

## ROS 2

```sh
ros2 pkg executables turtlesim
ros2 run turtlesim turtlesim_node

# rqt
rqt
rqt_graph

# topic
ros2 topic list -t
ros2 topic echo /turtle1/cmd_vel

# rosmsg
ros2 interface show geometry_msgs/msg/Twist

# topic
ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
ros2 topic echo /turtle1/pose
ros2 topic hz /turtle1/pose

#services
ros2 service list
ros2 interface show turtlesim/srv/Spawn
ros2 service call /clear std_srvs/srv/Empty


# params
ros2 param list
ros2 param get /turtlesim background_g

# load param file on node start
ros2 run <package_name> <executable_name> --ros-args --params-file <file_name>

# actions
ros2 action list -t
ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 1.57}"

# loglevel
ros2 run turtlesim turtlesim_node --ros-args --log-level WARN
```



### colcon
```sh
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build --symlink-install
colcon build --parallel-workers 2
colcon build --packages-select my_package

colcon test

ros2 pkg create

colcon test --packages-select YOUR_PKG_NAME --ctest-args -R YOUR_TEST_IN_PKG

ros2 pkg create --build-type ament_cmake --node-name my_node my_package
ros2 pkg create --build-type ament_python --node-name my_node my_package

```