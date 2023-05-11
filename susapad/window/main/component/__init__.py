import webbrowser

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from susapad import base_widgets as base
from . import buttons, header


README_LINK = "https://github.com/RickBarretto/SusaPadSoftware#readme"


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


class HelpButton(base.BaseFloatingButton):

    def __init__(self, window):
        super().__init__(window, "Ajuda", "F1")

    @QtCore.Slot()
    def action(self):
        webbrowser.open_new(README_LINK)


class WindowLayout(base.BaseFrame):

    def __init__(self, main_window):
        super().__init__()
        self.init_widgets(main_window)
        self.init_layout()
        self.init_help_button()

    def init_widgets(self, window):
        self.main_button  = buttons.ActionButton(window)
        self.close_button = buttons.CloseButton()

        self.group_header = HeaderGroup(main_window)

    def init_layout(self):

        bottom_layout = QtWidgets.QHBoxLayout()
        bottom_layout.addWidget(self.main)
        bottom_layout.addWidget(self.close)

        main_layout = QtWidgets.QVBoxLayout(self)

        main_layout.addWidget(self.group_header,
                alignment = Qt.AlignCenter | Qt.AlignTop)

        main_layout.addLayout(self.bottom_layout,
                alignment = Qt.AlignCenter | Qt.AlignBottom)

    def init_help_button(self):
        self.help_button = HelpButton(self)
        self.help_button.move(400, 20)
