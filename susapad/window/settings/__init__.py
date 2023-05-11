
import serial
from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

from susapad import widget

from . import ui
from .component import close


class SettingsWindow(widget.BaseWindow):

    def __init__(self, parent):
        super().__init__(parent.susapad, parent)

        self.ui = ui.SettingsUI(self, self.susapad)
        self.layout.addWidget(self.ui)

        self.close_button = close.CloseButton(self, parent)
        self.close_button.move(420, 20)
