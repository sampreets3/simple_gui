from rclpy.node import Node
import numpy as np

from example_interfaces.msg import Int32
from example_interfaces.srv import AddTwoInts

from PyQt5 import QtGui

class MyGuiNode(Node):
    def __init__(self, ui):
        super().__init__("ros2_hmi_node")
        self.ui = ui

        # Define our GUI button callbacks here
        self.ui.btn_publisher.clicked.connect(self.publisher_ros2_callback)

        # Define ROS2 publishers and subscribers here
        self._btn_publisher = self.create_publisher(Int32, '/chatter', 10)
        self._subscriber    = self.create_subscription(Int32, '/chatter', self.subscriber_callback, 1)

        # Define ROS 2 timers here
        self._timer         = self.create_timer(1.0, self.timer_callback)

        # Define internal member variables
        self._count         = 0
        self._robot_state   = [0.0, 0.0, 0.0]    # Store the robot's state [x, y, theta]

        # Sanity check
        self.get_logger().info("Node set up properly.")

    # Define the member functions here
    def publisher_ros2_callback(self):
        """
            This function is executed when we click the button
            on the GUI. So, this button should publish a message
            on the /chatter topic. This is what we will implement
            in the function body.
        """
        self._count = self._count + 1   # We increment the counter first

        # This part is standard ROS2 publisher code 
        msg = Int32()
        msg.data = self._count 
        self._btn_publisher.publish(msg)
        self.get_logger().info(f"[Publisher] I sent: {msg.data}")

    def subscriber_callback(self, msg):
        """
            The objective of this function is to set the text of the
            particular textLabel element when there is new data being
            received. Check the Qt documentation for more things you 
            can do to display the data.
        """
        temp = msg.data
        self.get_logger().info(f"[Subscriber] I heard: {temp}")
        self.ui.label_subscriber.setText(f"{msg.data}")

    def timer_callback(self): 
        """
            This timer will be used to update the information about the
            robot state. We will resort to publishing random numbers for
            the time being. 

            TODO    Listen to the odometry topic and update the values
            accordingly.
        """
        self._robot_state[0] = np.random.random()
        self._robot_state[1] = np.random.random()
        self._robot_state[2] = np.random.random()

        self.ui.robot_state_x.setText(f'{self._robot_state[0]:.4f}')
        self.ui.robot_state_y.setText(f'{self._robot_state[1]:.4f}')
        self.ui.robot_state_theta.setText(f'{self._robot_state[2]:.4f}')

        self.get_logger().info(f'Robot state: [x: {self._robot_state[0] :.4f}, y: {self._robot_state[1]:.4f}, theta: {self._robot_state[2]:.4f}]')


