"""Module for development purposes"""

import os, sys, pathlib

sys.path.append(
    os.path.dirname(
        pathlib.Path(os.path.realpath(__file__))\
        .parent.absolute()
    )
)

from PySide6 import QtWidgets

from susapad import window
from susapad.controller import keypad

def run_debug():
    """Start SusaPad Software in debug mode"""

    debug = True

    susapad = keypad.SusaPad(debug)
    susa_app = QtWidgets.QApplication([])
    susa_window = window.MainWindow(susapad)
    susa_window.show()
    sys.exit(susa_app.exec())
