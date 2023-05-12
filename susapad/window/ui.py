from __feature__ import true_property
from __feature__ import snake_case

import webbrowser

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from susapad import widget
from . import __component as component


README_LINK = "https://github.com/susapad/software#readme"

class MainUI(widget.BaseFrame):

    def __init__(self, main_window):
        super().__init__()
        self.init_widgets(main_window)
        self.init_layout()
        self.init_help_button()

    def init_widgets(self, window):
        self.app_logo       = component.SusaPadLogo()
        self.app_title      = component.SusaPadTitle()
        self.susapad_status = component.StatusLabel(window)

        self.main_button  = component.Action(window)
        self.close_button = component.Close()


    def init_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.add_layout(self.__init_header_layout())
        main_layout.add_layout(self.__init_bottom_layout())

    def __init_header_layout(self):
        header_alignment = Qt.AlignCenter | Qt.AlignTop
        header_layout = QtWidgets.QVBoxLayout()
        header_layout.add_widget(self.app_logo, alignment       =
                                header_alignment)
        header_layout.add_widget(self.app_title, alignment      =
                                header_alignment)
        header_layout.add_widget(self.susapad_status, alignment =
                                header_alignment)
        return header_layout

    def __init_bottom_layout(self):
        bottom_layout = QtWidgets.QHBoxLayout()
        bottom_layout.add_widget(self.main_button)
        bottom_layout.add_widget(self.close_button)
        return bottom_layout


    def init_help_button(self):
        self.help_button = component.Help(self, README_LINK)
        self.help_button.move(400, 20)
