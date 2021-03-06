#!/usr/bin/env python3
# Lets do more with PyQt5 :)

# import serious stuff
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel 
from PyQt5.QtCore import Qt


# The class where everything happens
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        # Initialize QMainWindow object 
        super(MainWindow, self).__init__(*args, **kwargs) 

        # Set Window title
        self.setWindowTitle("My awesome App")
        
        # Add a label widget
        label = QLabel("UNIX is love!")
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget
        self.setCentralWidget(label)


# Initialize the application
app = QApplication(sys.argv)

# Create a window and show it
window = MainWindow()
window.show()

# Start the event loop
app.exec_()

