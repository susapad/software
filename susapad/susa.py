"""SusaPad's main file"""

import sys

from PySide6 import QtWidgets

from susa.ui import main_window


def run():
    """Start SusaPad's application"""
    
    susa_app = QtWidgets.QApplication([])
    susa_window = main_window.MainWindow()
    susa_window.resize(300, 500)
    susa_window.show()
    sys.exit(susa_app.exec())


if __name__ == "__main__":
    run()
