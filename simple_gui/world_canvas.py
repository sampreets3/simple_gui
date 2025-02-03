"""
Displays a world canvas
"""

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

class WorldCanvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def plot_data(self, x, y):
        self.ax.clear()
        self.ax.plot(x, y, marker='o', linestyle='-')
        self.canvas.draw()