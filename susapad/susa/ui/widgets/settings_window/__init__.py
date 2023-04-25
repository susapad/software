from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt

from . import rapid_trigger


class FormsGroup(QtWidgets.QWidget):

    def __init__(self, window, susapad):
        super().__init__()

        self.activate_toggle = rapid_trigger\
            .RapidTriggerButton(window, susapad)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.activate_toggle)



class WindowLayout(QtWidgets.QFrame):

    def __init__(self, window, susapad):
        super().__init__()

        self.setObjectName("background-frame")
        self.__init_style()

        self.forms = FormsGroup(window, susapad)
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.forms)


    def __init_style(self):
        self.setStyleSheet(
            """

            QFrame {
                border-radius: 20px;
                background-color: #121212;
            }

            QPushButton {
                    background-color: #0e639e;
                    border-radius: 15px;
                    min-width: 10em;
                    padding: 6px;
                    font: bold;
                    color: white;
                }

            QPushButton:hover {
                background-color: #127ecb;
            }

            """
        )
        self.setContentsMargins(20, 20, 20, 20)
