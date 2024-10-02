from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    ros2_hmi_node = Node(
        package = 'simple_gui',
        executable='ros2_hmi_node',
    )

    add_two_ints_server = Node(
        package='simple_gui',
        executable='add_two_ints_server'
    )

    ld.add_action(ros2_hmi_node)
    ld.add_action(add_two_ints_server)

    return ld