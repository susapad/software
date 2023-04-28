
import serial
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

from susapad.base_widgets import window

from . import widgets


class SettingsWindow(window.BaseWindow):

    def __init__(self, parent):

        super().__init__(parent.susapad, parent)

        self.is_on: bool = True
        self.rts: int = 200

        self.settings_widget = widgets.WindowLayout(self, self.susapad)
        self.layout.addWidget(self.settings_widget)

        self.close_button = widgets.CloseButton(self, parent)
