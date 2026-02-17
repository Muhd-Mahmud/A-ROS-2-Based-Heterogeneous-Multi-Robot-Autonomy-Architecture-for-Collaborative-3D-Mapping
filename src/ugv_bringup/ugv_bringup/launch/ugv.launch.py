import os

from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Robot (MTREBot)
    robot_share = get_package_share_directory('mtrebot_description')
    urdf_path = os.path.join(robot_share, 'urdf', 'mtrebot.urdf')
    robot_desc = open(urdf_path, 'r', encoding='utf-8').read()

    # World (keep your existing ugv_world)
    world_share = get_package_share_directory('ugv_description')
    world_path = os.path.join(world_share, 'worlds', 'ugv_world.sdf')

    gazebo = ExecuteProcess(
        cmd=['ign', 'gazebo', '-r', world_path],
        output='screen'
    )

    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc}]
    )

    spawn = ExecuteProcess(
        cmd=[
            'ros2', 'run', 'ros_gz_sim', 'create',
            '-name', 'mtrebot',
            '-x', '0', '-y', '0', '-z', '0.2',
            '-string', robot_desc
        ],
        output='screen'
    )

    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        output='screen',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
            '/odom@nav_msgs/msg/Odometry@gz.msgs.Odometry',
            '/scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan'
        ]
    )

    return LaunchDescription([gazebo, rsp, spawn, bridge])
