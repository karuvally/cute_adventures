#!/usr/bin/env python3
# Lets test signals (and slots)...

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

        # Call our custom method when WindowTitle changes
        self.windowTitleChanged.connect(self.onWindowTitleChange)

        # Change the window title
        self.setWindowTitle("My awesome app!")

    # This method gets called when window title gets changed
    def onWindowTitleChange(self, new_title):
        print("The new title is,", new_title)


# Initialize the application
app = QApplication(sys.argv)

# Create a window and show it
window = MainWindow()
window.show()

# Start the event loop
app.exec_()

