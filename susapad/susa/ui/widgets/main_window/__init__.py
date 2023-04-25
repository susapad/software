from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt

from . import buttons, header


class HeaderGroup(QtWidgets.QWidget):

    def __init__(self, main_window):
        super().__init__()

        self.logo   = header.SusaPadLogo()
        self.title  = header.SusaPadTitle()
        self.status = header.StatusLabel(main_window)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.logo,
                alignment = Qt.AlignCenter | Qt.AlignTop)
        self.layout.addWidget(self.title,
                alignment = Qt.AlignCenter | Qt.AlignTop)
        self.layout.addWidget(self.status,
                alignment = Qt.AlignCenter | Qt.AlignTop)


class ButtonGroup(QtWidgets.QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main  = buttons.ActionButton(main_window)
        self.close = buttons.CloseButton()

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.main)
        self.layout.addWidget(self.close)


class WindowLayout(QtWidgets.QFrame):

    def __init__(self, main_window):
        super().__init__()

        # Configuration
        self.setObjectName("background-frame")
        self.__init_style()

        self.group_header = HeaderGroup(main_window)
        self.group_button = ButtonGroup(main_window)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.group_header, 
                alignment = Qt.AlignCenter | Qt.AlignTop)
        self.layout.addWidget(self.group_button, 
                alignment = Qt.AlignCenter | Qt.AlignBottom)

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

                QPushButton:pressed {
                    background-color: #0a4874;
                }

                QPushButton[accessibleName="secondary"] {
                    background-color: #b71970;
                }

                QPushButton:hover[accessibleName="secondary"] {
                    background-color: #dd1e87;
                }

                QPushButton:pressed[accessibleName="secondary"] {
                    background-color: #861252;
                }
            """
        )
        self.setContentsMargins(20, 20, 20, 20)
