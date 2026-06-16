import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = get_package_share_directory('hospital_robot_slam')
    cartographer_config_dir = os.path.join(pkg_share, 'config')

    return LaunchDescription([
        # Cartographer SLAM Node
        Node(
            package='cartographer_ros',
            executable='cartographer_node',
            name='cartographer_node',
            output='screen',
            parameters=[{'use_sim_time': True}],
            arguments=['-configuration_directory', cartographer_config_dir,
                       '-configuration_basename', 'cartographer_params.lua']
        ),
        # 5cm (0.05m) Occupancy Grid Node (Raporla Birebir Uyumlu)
        Node(
            package='cartographer_ros',
            executable='cartographer_occupancy_grid_node',
            name='cartographer_occupancy_grid_node',
            output='screen',
            parameters=[{'use_sim_time': True}, {'resolution': 0.05}]
        ),
        # RViz2 Görselleştirme
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(cartographer_config_dir, 'hospital.rviz')]
        ),
    ])
