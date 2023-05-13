"""SusaPad's main file"""

import os, sys, pathlib

sys.path.append(
    os.path.dirname(
        pathlib.Path(os.path.realpath(__file__))\
        .parent.absolute()
    )
)

from PySide6 import QtWidgets

from susapad.windows import main
from susapad.controller import susapad as susapad_module
from susapad import translations as ts


def debug():
    """Start SusaPad's application"""

    susapad = susapad_module.SusaPad(True)
    susa_app = QtWidgets.QApplication([])
    susa_window = main.MainWindow(susapad, ts.get_language())
    susa_window.show()
    sys.exit(susa_app.exec())


def debug_insider():
    """Start SusaPad's application"""

    susapad = susapad_module.SusaPad(True)
    susapad.insider = True
    susa_app = QtWidgets.QApplication([])
    susa_window = main.MainWindow(susapad, ts.get_language())
    susa_window.show()
    sys.exit(susa_app.exec())
