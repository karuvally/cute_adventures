#!/usr/bin/env python3

# import serious stuff
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow 


# Initialize the application
app = QApplication(sys.argv)

# Create a window and show it
window = QMainWindow()
window.show()

# Start the event loop
app.exec_()

