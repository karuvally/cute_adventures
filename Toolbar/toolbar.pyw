#!/usr/bin/env python3
# Testing events

# Import serious stuff
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar
from PyQt5.QtWidgets import QAction
from PyQt5.QtCore import Qt


# The class where everything happens
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        # Initialize QMainWindow object
        super(MainWindow, self).__init__(*args, **kwargs)

        # Set Window title
        self.setWindowTitle("I have a toolbar!")

        # Setup toolbar
        toolbar = QToolBar("main_toolbar")
        self.addToolBar(toolbar)

        # Setup QAction
        button_action = QAction("Your button", self)
        button_action.setStatusTip("This is the button!")
        button_action.triggered.connect(self.on_button_click)
        toolbar.addAction(button_action)

    # Define what happens when toolbar gets clicked
    def on_button_click(self, string):
        print("Click", string)


# Initialize the application
app = QApplication(sys.argv)

# Create a window and show it
window = MainWindow()
window.show()

# Start the event loop
app.exec_()
