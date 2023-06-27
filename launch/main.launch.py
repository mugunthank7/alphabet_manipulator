import os
import xacro
from ament_index_python.packages import get_package_share_directory

from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.parameter_descriptions import ParameterFile

def generate_launch_description():
    
    pkg_path = os.path.join(get_package_share_directory('alphabet_manipulator'))
    xacro_file = os.path.join(pkg_path, 'urdf', 'bot.urdf')
    robot_description_config = xacro.process_file(xacro_file).toxml()
    
    gazebo_params_file = os.path.join(get_package_share_directory('alphabet_manipulator'), 'gazebo_params.yaml')
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ]), launch_arguments={'extra_gazebo_args': '--ros-args --params-file ' + gazebo_params_file}.items()
    )
    
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    params = {'robot_description': robot_description_config, 'use_sim_time': use_sim_time}
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params]
    )
    
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', '/robot_description',
                   '-entity', 'bot'],
        output='screen'
    )
    
    controller_manager = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["arm_controller"]
    )

    return LaunchDescription([
        node_robot_state_publisher,
        gazebo,
        spawn_entity,
        controller_manager
    ])
