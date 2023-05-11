
import serial
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

from susapad import widget

from . import ui


class SettingsWindow(widget.BaseWindow):

    def __init__(self, parent):
        super().__init__(parent.susapad, parent)

        self.ui = ui.SettingsUI(self, self.susapad)
        self.layout.addWidget(self.settings_widget)

        self.close_button = ui.CloseButton(self, parent)
        self.close_button.move(420, 20)
