# TP 1 : 

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

## ROS commands

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


## Package making

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

