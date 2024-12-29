from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # Start Gazebo simulator
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '/usr/share/gazebo-11/worlds/empty.world'],
            output='screen'
        ),
        # Spawn the robot in Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'my_robot',
                '-file', '/home/daniel/ros2_ws/src/my_robot/urdf/robot.urdf'
            ],
            output='screen'
        )
    ])
