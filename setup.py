import os
from setuptools import setup
from glob import glob

package_name = 'simple_gui'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    py_modules=['simple_gui.simple_gui'],
    maintainer='Sampreet SARKAR',
    maintainer_email='sampreets3@gmail.com',
    description='Simple GUI demo application for ROS2 using PyQt5',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ros2_hmi_node = simple_gui.main:main',
            'add_two_ints_server = simple_gui.add_two_ints_server:main'
        ],
    },
)
