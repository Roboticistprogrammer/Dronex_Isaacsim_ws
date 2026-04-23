Prerequisits:
Download ROS 2 following the instructions on the official website:

ROS 2 Humble Ubuntu 22.04

(Optional) Some message types (Detection2DArray and Detection3DArray used for publishing bounding boxes) in the ROS 2 Bridge depend on the vision_msgs_package. Run the command below to install the package on your system. If you have built ROS 2 from source, clone the package and include it in your ROS 2 installation workspace before re-building. If you don’t need to run the vision_msgs publishers, you can skip this step.

sudo apt install ros-humble-vision-msgs
(Optional) Some message types (AckermannDriveStamped used for publishing and subscribing to Ackermann steering commands) in the ROS 2 Bridge depend on the ackermann_msgs_package. Run the command below to install the package on your system. If you have built ROS 2 from source, clone the package and include it in your ROS 2 installation workspace before re-building. If you don’t need to run the ackermann_msgs publishers/subscribers, you can skip this step.

sudo apt install ros-humble-ackermann-msgs
Ensure that the ROS environment is sourced in the terminal or in your ~/.bashrc file. You must perform this step each time and before using any ROS commands.

source /opt/ros/humble/setup.bash

Sourcing Terminal:
export isaac_sim_package_path=$HOME/isaacsim

export ROS_DISTRO=humble

export RMW_IMPLEMENTATION=rmw_fastrtps_cpp

# Can only be set once per terminal.
# Setting this command multiple times will append the internal library path again potentially leading to conflicts
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$isaac_sim_package_path/exts/isaacsim.ros2.bridge/humble/lib

# Run Isaac Sim
$isaac_sim_package_path/isaac-sim.sh

Building Steps:
To build the ROS 2 workspace, you might need to install additional packages:

# For rosdep install command
sudo apt install python3-rosdep build-essential
# For colcon build command
sudo apt install python3-colcon-common-extensions
Ensure that your native ROS 2 has been sourced:

source /opt/ros/humble/setup.bash
Resolve any package dependencies from the root of the ROS 2 workspace by running the following commands:

cd humble_ws
git submodule update --init --recursive # If using docker, perform this step outside the container and relaunch the container
rosdep install -i --from-path src --rosdistro humble -y
Build the workspace:

colcon build
Under the root directory, new build, install, and log directories are created.

To start using the ROS 2 packages built within this workspace, open a new terminal and source the workspace with the following commands:

source /opt/ros/humble/setup.bash
cd humble_ws
source install/local_setup.bash
