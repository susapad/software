
import serial
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

from susapad.ui.widgets import settings_window
from susapad.base_widgets import window
from susapad.ui.widgets.settings_window import close


class SettingsWindow(window.BaseWindow):

    def __init__(self, parent):

        super().__init__(parent.susapad, parent)

        self.is_on: bool = True
        self.rts: int = 200

        self.settings_widget = settings_window.WindowLayout(self, self.susapad)
        self.layout.addWidget(self.settings_widget)

        self.close_button = close.CloseButton(self, parent)
