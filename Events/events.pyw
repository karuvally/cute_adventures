#!/usr/bin/env python3
# Testing events

# Import serious stuff
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt


# The class where everything happens
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        # Initialize QMainWindow object
        super(MainWindow, self).__init__(*args, **kwargs)

        # Set Window title
        self.setWindowTitle("My events app")

    def contextMenuEvent(self, event):
        print("Context menu event was invoked")


# Initialize the application
app = QApplication(sys.argv)

# Create a window and show it
window = MainWindow()
window.show()

# Start the event loop
app.exec_()