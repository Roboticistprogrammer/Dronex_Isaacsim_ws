from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os


DEFAULT_WAREHOUSE_USD = (
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/"
    "Assets/Isaac/5.1/Isaac/Environments/Simple_Warehouse/warehouse_multiple_shelves.usd"
)


def generate_launch_description():
    isaac_sim_launch_dir = get_package_share_directory("isaacsim")

    # If standalone is provided, Isaac Sim runs that script (GUI scene arg is ignored).
    # Use this to start a Pegasus script that spawns an Iris multirotor, e.g.:
    # ros2 launch dronex_bringup warehouse_simulation.py standalone:=/abs/path/pegasus_warehouse_iris.py
    return LaunchDescription([
        DeclareLaunchArgument(
            "gui",
            default_value=DEFAULT_WAREHOUSE_USD,
            description="USD scene path for GUI mode (warehouse_multiple_shelves).",
        ),
        DeclareLaunchArgument(
            "standalone",
            default_value="",
            description="Optional standalone Python script (Pegasus workflow).",
        ),
        DeclareLaunchArgument(
            "version",
            default_value="5.1.0",
            description="Isaac Sim version (ignored when install_path is set in included launch).",
        ),
        DeclareLaunchArgument(
            "play_sim_on_start",
            default_value="true",
            description="Start simulation after scene/script loads.",
        ),
        DeclareLaunchArgument(
            "use_internal_libs",
            default_value="true",
            description="Use Isaac Sim internal ROS Python libs (recommended for Isaac Sim 5.1).",
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(isaac_sim_launch_dir, "launch", "run_isaacsim.launch.py")
            ),
            launch_arguments={
                "gui": LaunchConfiguration("gui"),
                "standalone": LaunchConfiguration("standalone"),
                "version": LaunchConfiguration("version"),
                "play_sim_on_start": LaunchConfiguration("play_sim_on_start"),
                "use_internal_libs": LaunchConfiguration("use_internal_libs"),
            }.items()
        )
    ])

