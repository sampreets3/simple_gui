"""
Displays a world canvas
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvasQTAgg
from PyQt5.QtWidgets import QWidget, QVBoxLayout

class WorldCanvas(QWidget):
    """
    We created our custom widget called WorldCanvas in QT Designer.

    Now we implement the class and the necessary behaviour of the 
    widget. Note that this class exposes a couple of useful functions
    to enable interaction with the outside world. 
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasQTAgg(self.figure)
        
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_xlim(-10, 10)  # TODO Dynamically scale maps?
        self.ax.set_ylim(-10, 10)  # TODO Dynamically scale maps? 
        self.ax.set_aspect("equal")

    def plot_robot_pose(self, x : float, y : float, theta : float) -> None:
        """
        Plots the robot's pose on the map. 
        """
        self.ax.clear()
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        
        self.ax.plot(x, y, scalex=2.0, scaley=2.0, marker='o', linestyle='-', label='Robot Position')
        arrow_length = 1.0
        dx = arrow_length * np.cos(theta)
        dy = arrow_length * np.sin(theta)
        self.ax.arrow(x, y, dx, dy, head_width=0.1, head_length=0.1, fc='r', ec='r', label='Robot Orientation')
        
        self.canvas.draw()