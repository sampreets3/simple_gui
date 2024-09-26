from setuptools import setup

package_name = 'simple_gui'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    py_modules=['simple_gui.simple_gui'],
    maintainer='Sampreet SARKAR',
    maintainer_email='sampreet.sarkar@cea.fr',
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
