
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt

import serial

from .widgets import settings_window
from .widgets.common import window


class SettingsWindow(window.BaseWindow):

    def __init__(self, parent):

        super().__init__(parent.susapad, parent)

        self.is_on: bool = True
        self.rts: int = 200

        self.settings_widget = settings_window.WindowLayout(self.susapad)
        self.layout.addWidget(self.settings_widget)
        

    @QtCore.Slot()
    def rapid_trigger_sensibility(self, sensibility: int):
        pass

    @QtCore.Slot()
    def save_settings(self):
        pass
