from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt

from . import buttons, header


class HeaderGroup(QtWidgets.QWidget):

    def __init__(self, window):
        super().__init__()

        self.logo   = header.SusaPadLogo()
        self.title  = header.SusaPadTitle()
        self.status = header.StatusLabel(window)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.logo,
                alignment = Qt.AlignCenter | Qt.AlignTop)
        self.layout.addWidget(self.title,
                alignment = Qt.AlignCenter | Qt.AlignTop)
        self.layout.addWidget(self.status,
                alignment = Qt.AlignCenter | Qt.AlignTop)


class ButtonGroup(QtWidgets.QWidget):
    def __init__(self, window):
        super().__init__()
        self.main  = buttons.ActionButton(window)
        self.close = buttons.CloseButton()

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.main)
        self.layout.addWidget(self.close)


class WindowLayout(QtWidgets.QFrame):

    def __init__(self, window):
        super().__init__()

        # Configuration
        self.setObjectName("background-frame")
        self.__init_style()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(HeaderGroup(window), 
                alignment = Qt.AlignCenter | Qt.AlignTop)
        self.layout.addWidget(ButtonGroup(window), 
                alignment = Qt.AlignCenter | Qt.AlignBottom)

    def __init_style(self):
        self.setStyleSheet(
            """
                border-radius: 20px;
                background-color: #121212;
            """
        )
        self.setContentsMargins(20, 20, 20, 20)
