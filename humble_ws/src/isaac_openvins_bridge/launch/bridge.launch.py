from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Path to your custom config file
    config_path = os.path.join(
        get_package_share_directory('isaac_openvins_bridge'),
        'config',
        'isaac_sensor.yaml'
    )

    return LaunchDescription([
        Node(
            package='ov_msckf',
            executable='ov_msckf_node',
            name='vio_estimator',
            output='screen',
            parameters=[{
                "config_path": config_path,
                "verbosity": "INFO",
                "use_stereo": True  # Set to False if using monocular
            }],
            # THIS IS THE "MAPPING" STEP
            remappings=[
                ('/ov_msckf/imu0', '/sim/imu'),                 # Map OpenVINS IMU -> Isaac IMU
                ('/ov_msckf/cam0/image_raw', '/sim/left/image'),# Map OpenVINS Cam0 -> Isaac Left Cam
                ('/ov_msckf/cam1/image_raw', '/sim/right/image')# Map OpenVINS Cam1 -> Isaac Right Cam
            ]
        )
    ])

Note:
Scenario:
Isaac Sim publishes: /sim/left_camera/image, /sim/imu
OpenVINS expects: /cam0/image_raw, /imu0
