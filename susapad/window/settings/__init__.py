from __feature__ import true_property
from __feature__ import snake_case

import serial
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

from susapad import widget

from . import ui
from .component import close


class SettingsWindow(widget.BaseWindow):

    def __init__(self, parent):
        super().__init__(parent.susapad, parent)
        self.init_widgets()
        self.init_layout(parent)

    def init_widgets(self):
        self.ui = ui.SettingsUI(self, self.susapad)

    def init_layout(self, parent):
        self.layout.add_widget(self.ui)
        self.__init_close_button(parent)

    def __init_close_button(self, parent):
        self.close_button = close.CloseButton(self, parent)
        self.close_button.move(420, 20)
