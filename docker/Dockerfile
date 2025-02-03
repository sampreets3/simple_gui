FROM osrf/ros:humble-desktop-full-jammy

RUN mkdir -p /home/ros2_ws/src && apt-get update && apt-get install -y terminator python3 python3-pip

RUN python3 -m pip install pyqt5

RUN echo 'source /home/ros2_ws/install/setup.bash' >> ~/.bashrc && \
    apt-get update && rm -rf /var/lib/apt/lists/* && \
    apt-get clean

RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    cd /home/ros2_ws && \
    colcon build

ADD startup.sh /startup.sh
RUN chmod +x /startup.sh
ENTRYPOINT ["/startup.sh"]
CMD ["/bin/bash"]