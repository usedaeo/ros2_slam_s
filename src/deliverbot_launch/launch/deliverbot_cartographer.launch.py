import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
   my_cartographer = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('myrobot_cartographer'), 'launch'),
         '/cartographer.launch.py'])
      )

   ld = LaunchDescription()
   #cartographer
   ld.add_action(my_cartographer)
 
   
   return ld