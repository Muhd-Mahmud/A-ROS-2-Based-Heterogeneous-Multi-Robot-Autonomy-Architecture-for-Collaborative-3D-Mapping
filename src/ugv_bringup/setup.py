from setuptools import setup
import os
from glob import glob

package_name = 'ugv_bringup'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('ugv_bringup/launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mahmud',
    maintainer_email='mahmudmuhammed811@gmail.com',
    description='UGV bringup (Gazebo + spawn + bridge) for ROS 2 Humble',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={'console_scripts': []},
)
