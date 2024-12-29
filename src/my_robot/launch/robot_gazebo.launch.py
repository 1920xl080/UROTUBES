from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '/usr/share/gazebo-11/worlds/empty.world'],
            output='screen'
        ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'r0bot',
                '-file', '/home/user/ros2_ws/src/my_robot/urdf/simple_robot.urdf'
            ],
            output='screen'
        )
    ])

