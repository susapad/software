
import serial
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

from susapad.susa.ui.widgets import settings_window
from susapad.susa.ui.widgets.common import window


class SettingsWindow(window.BaseWindow):

    def __init__(self, parent):

        super().__init__(parent.susapad, parent)

        self.is_on: bool = True
        self.rts: int = 200

        self.settings_widget = settings_window.WindowLayout(self, self.susapad)
        self.layout.addWidget(self.settings_widget)

    @QtCore.Slot()
    def save_settings(self):
        pass
