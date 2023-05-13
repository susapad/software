import webbrowser

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from susapad import base_widgets as base
from . import buttons, header


README_LINK = "https://github.com/susapad/software#readme"


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
    def __init__(self, main_window, language: dict):
        super().__init__()
        self.main  = buttons.ActionButton(main_window, language)
        self.close = buttons.CloseButton(language)

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.main)
        self.layout.addWidget(self.close)

class HelpButton(base.BaseFloatingButton):

    def __init__(self, window, language: dict):
        super().__init__(window, language["buttons"]["help"], "F1")

    @QtCore.Slot()
    def action(self):
        webbrowser.open_new(README_LINK)


class WindowLayout(base.BaseFrame):

    def __init__(self, main_window, language: dict):
        super().__init__()

        self.group_header = HeaderGroup(main_window)
        self.group_button = ButtonGroup(main_window, language)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.group_header,
                alignment = Qt.AlignCenter | Qt.AlignTop)
        self.layout.addWidget(self.group_button,
                alignment = Qt.AlignCenter | Qt.AlignBottom)

        self.help_button = HelpButton(self, language)
        self.help_button.move(400, 20)
