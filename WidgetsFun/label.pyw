#!/usr/bin/env python3
# Trying to implement a simple label widget

# Import serious stuff
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


# Setup the class which will define the MainWindow
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        


# Initialize the application
app = QApplication(sys.argv)

# Create a window and show it
window = MainWindow()
window.show()

# Star the event loop
app.exec_()