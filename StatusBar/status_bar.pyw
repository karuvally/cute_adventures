#!/usr/bin/env python3
# Implementing a status bar

# Import serious stuff
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar
from PyQt5.QtWidgets import QAction, QStatusBar


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

        # Setup QAction for the Click! button
        button_action = QAction("Click!", self)
        button_action.setStatusTip("This is the button!")
        button_action.triggered.connect(self.on_button_click)
        toolbar.addAction(button_action)

        # Setup statusbar
        self.setStatusBar(QStatusBar(self))

    # Define what happens when toolbar gets clicked
    def on_button_click(self, bool_value):
        print("Click", bool_value)


# Initialize the application
app = QApplication(sys.argv)

# Create a window and show it
window = MainWindow()
window.show()

# Start the event loop
app.exec_()
