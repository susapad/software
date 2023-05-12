from __feature__ import true_property
from __feature__ import snake_case

import webbrowser

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from susapad import widget
from .__component import buttons, header


README_LINK = "https://github.com/RickBarretto/SusaPadSoftware#readme"


class HelpButton(widget.BaseFloatingButton):

    def __init__(self, window):
        super().__init__(window, "Ajuda", "F1")

    @QtCore.Slot()
    def action(self):
        webbrowser.open_new(README_LINK)


class MainUI(widget.BaseFrame):

    def __init__(self, main_window):
        super().__init__()
        self.init_widgets(main_window)
        self.init_layout()
        self.init_help_button()

    def init_widgets(self, window):
        self.app_logo       = header.SusaPadLogo()
        self.app_title      = header.SusaPadTitle()
        self.susapad_status = header.StatusLabel(window)

        self.main_button  = buttons.ActionButton(window)
        self.close_button = buttons.CloseButton()


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
        self.help_button = HelpButton(self)
        self.help_button.move(400, 20)
