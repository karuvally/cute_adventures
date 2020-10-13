#!/usr/bin/env python3
# Fun with some of the widgets Qt5 provides

# Import serious stuff
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


# Our main class
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        # Initialize the main window
        super(MainWindow, self).__init__(*args, **kwargs)
        
        # Set title for our window
        self.setWindowTitle("Awesome App 2.0")

        # Set the layout and widgets
        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit
        ]
        
        # Add each of the widgets to the layout
        for w in widgets:
            layout.addWidget(w)
        
        # Setup a QWidget object and add the layout to QWidget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


# Setup the QApplication instance
app = QApplication(sys.argv)

# Setup and show the window
window = MainWindow()
window.show()

# Start the event loop
app.exec_()
