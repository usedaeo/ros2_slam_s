import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.actions import TimerAction
def generate_launch_description():
   gazebo = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('deliverbot_description'), 'launch'),
         '/mygazebo.launch.py']),
         launch_arguments={'use_sim_time': 'true'}.items(),
      )
   laser_odom = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('rf2o_laser_odometry'), 'launch'),
         '/rf2o_laser_odometry.launch.py'])
      )
   odom_ekf = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('robot_localization'), 'launch'),
         '/ekf.launch.py'])
      )
   laser_odom_L = Node(package='chulilaser', 
                       executable='mylaser',
                    output='screen')
   
   depthimage_to_laserscan1 = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('depthimage_to_laserscan'), 'launch'),
         '/depthimage_to_laserscan-launch.py'])
      )
   ira_laser = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('ira_laser_tools'), 'launch'),
         '/laserscan_multi_merger.launch.py'])
      )

   ld = LaunchDescription()
   #仿真环境
   ld.add_action(gazebo)
   #雷达里程计
   ld.add_action(laser_odom)
   #里程计融合  雷达  轮式  IMU
   # ld.add_action(odom_ekf)

    #雷达初步处理
   ld.add_action(laser_odom_L)
   #深度转激光
   ld.add_action(depthimage_to_laserscan1)
   # #雷达融合
   ld.add_action(
      TimerAction(
         period=2.0,
         actions=[odom_ekf]
            )
   )
   #里程计融合  雷达  轮式  IMU
   # ld.add_action(odom_ekf)
   # ld.add_action(ira_laser)
   
   return ld